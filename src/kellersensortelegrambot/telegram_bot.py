from telegram.ext import Updater, CommandHandler
import Adafruit_DHT
import os
from os import walk
import threading
import serial
from enum import Enum


class CableState(Enum):
    """
    Enum for cable states
    """
    NONE = 0
    RUNNING = 1
    DISCONNECTED = 2
    WATER_DETECTED = 3
    CABEL_DIRECT_CONNECTION = 4


class BackgroundThread(threading.Thread):
    """
    Background thread for listining on the arduino serial port
    """

    def __init__(self, usb_port, updater):
        threading.Thread.__init__(self)
        self.usb_port = usb_port
        self.updater = updater
        self.cable_state = CableState(CableState.RUNNING)

    def run(self) -> None:
        """
        start the threat
        """

        print("Starting " + self.usb_port)
        ser = serial.Serial(self.usb_port, 9600)  # listen on arduino serial port

        while True:
            # make the arduino output readable
            output = ser.readline().decode("utf-8").lower()
            # print('%s %s' % (self.usb_port, output))
            value = output.replace(" nf\r\n", "")

            if value == "inf":  # -> CABEL_DIRECT_CONNECTION
                if self.cable_state != CableState.CABEL_DIRECT_CONNECTION:
                    self.cable_state = CableState.CABEL_DIRECT_CONNECTION
                    text = ('Kabel ist kurzgeschlossen @ Arduino %s!' % self.usb_port)
                    print(text)
                    self.updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text=text)
            elif float(value) < 0.001:  # -> DISCONNECTED
                if self.cable_state != CableState.DISCONNECTED:
                    self.cable_state = CableState.DISCONNECTED
                    text = ('Kein Kabel @ Arduino %s angeschlossen!' % self.usb_port)
                    print(text)
                    self.updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text=text)
            elif float(value) <= 30000:  # -> CABEL_DIRECT_CONNECTION
                if self.cable_state != CableState.RUNNING:
                    self.cable_state = CableState.RUNNING
                    text = ('Kabel @ Arduino %s keine Probleme gefunden!' % self.usb_port)
                    self.updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text=text)
            else:  # -> WATER_DETECTED
                if self.cable_state != CableState.WATER_DETECTED:
                    self.cable_state = CableState.WATER_DETECTED
                    text = ('Wasser @ Arduino %s gefunden!' % self.usb_port)
                    print(text)
                    self.updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text=text)

    def sensor_test(self) -> None:
        """
        reset cable state to post the current cable state
        """
        self.cable_state = CableState(CableState.NONE)


class BotDaemon:
    """
    Telegram Bot Daemon
    """

    def __init__(self):
        # create empty array for all arduino devices
        self.sensor_threats = []

        # setup telegram daemon
        self.updater = Updater(os.environ['BOT_ID'])
        # set bot commands to functions
        self.updater.dispatcher.add_handler(CommandHandler('hilfe', self.help))
        self.updater.dispatcher.add_handler(CommandHandler('temperatur', self.temperature))
        self.updater.dispatcher.add_handler(CommandHandler('luftfeuchtigkeit', self.humidity))
        self.updater.dispatcher.add_handler(CommandHandler('wassermelder', self.water_request))

        # start water detection background threats for each arduino
        self.start_water_detection_background()

        # waiting for telegram commands
        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def help(bot, update) -> None:
        """
        telegram command
        show all possible commands
        """
        update.message.reply_text('/hilfe /temperatur /luftfeuchtigkeit /wassermelder')

    @staticmethod
    def temperature(bot, update) -> None:
        """
        telegram command
        show the current temperature
        """
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor, pin)
        update.message.reply_text('Temperatur: {0:.2f}'.format(round(temperature_data, 2)))

    @staticmethod
    def humidity(bot, update) -> None:
        """
        telegram command
        show the current humidity
        """
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor, pin)
        update.message.reply_text('Luftfeuchtigkeit: {0:.2f}'.format(round(humidity_data, 2)))

    def water_request(self, bot, update) -> None:
        """
        telegram command
        run sensor test for each arduino threat
        """
        update.message.reply_text('Wassersensor Test!')
        for thread in self.sensor_threats:
            thread.sensor_test()

    @staticmethod
    def list_all_usb_ports() -> []:
        """
        return all usb device for the raspberry pi
        Returns:
            all usb devices as string array
        """
        usb_ports = []
        path = "/dev/"
        for (dirpath, dirnames, filenames) in walk(path):
            for file in filenames:
                if file.startswith("ttyUSB"):
                    usb_ports.append(os.path.join(path, file))
        return usb_ports

    def start_water_detection_background(self) -> None:
        """
        start for each arduino usb device a background threat and store the threats in the sensor_threats array
        """
        for usb_port in self.list_all_usb_ports():
            try:
                thread = BackgroundThread(usb_port, self.updater)
                thread.start()
                self.sensor_threats.append(thread)
            except:
                print("Error: unable to start thread")
