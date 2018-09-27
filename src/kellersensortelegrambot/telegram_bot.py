from telegram.ext import Updater, CommandHandler
import Adafruit_DHT
import os

import RPi.GPIO as GPIO


def run_bot():
    def help(bot, update):
        update.message.reply_text('/help /temperature /humidity /water')

    def temperature(bot, update):
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor, pin)
        update.message.reply_text('Temperatur: {0:.2f}'.format(round(temperature_data, 2)))

    def humidity(bot, update):
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity_data, temperature_data = Adafruit_DHT.read_retry(sensor, pin)
        update.message.reply_text('Luftfeuchtigkeit: {0:.2f}'.format(round(humidity_data, 2)))

    def water_detection():
        GPIO.setmode(GPIO.BOARD)  # Set GPIO pin numbering

        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(21)
        if not input_state:  # Check whether pin is grounded
            updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text='Wasser @ Kabel 1 gefunden!')

        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(13)
        if not input_state:  # Check whether pin is grounded
            updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text='Wasser @ Kabel 2 gefunden!')

        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        input_state = GPIO.input(23)
        if not input_state:  # Check whether pin is grounded
            updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text='Wasser @ Kabel 3 gefunden!')

    def water(bot, update):
        update.message.reply_text('Wasser Sensor test!')
        water_detection()

    def water_job(bot, job):
        water_detection()

    updater = Updater(os.environ['BOT_ID'])
    job = updater.job_queue

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('temperature', temperature))
    updater.dispatcher.add_handler(CommandHandler('humidity', humidity))
    updater.dispatcher.add_handler(CommandHandler('water', water))

    # enable for cronjob
    job_minute = job.run_repeating(water_job, interval=60, first=0)

    updater.start_polling()
    updater.idle()
