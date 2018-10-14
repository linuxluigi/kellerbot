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

    def water_detection(pin):
        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        input_state = GPIO.input(pin)
        if input_state:  # Check whether pin is grounded
            updater.bot.send_message(chat_id=os.environ['CHAT_ID'], text=('Wasser @ Pin %d gefunden!' % pin))
        GPIO.cleanup()

    def water():
        water_detection(12)
        water_detection(16)
        water_detection(18)

    def water_request(bot, update):
        update.message.reply_text('Wassersensor Test!')
        water()

    def water_job(bot, job):
        water()

    updater = Updater(os.environ['BOT_ID'])
    job = updater.job_queue

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('temperature', temperature))
    updater.dispatcher.add_handler(CommandHandler('humidity', humidity))
    updater.dispatcher.add_handler(CommandHandler('water', water_request))

    # enable for cronjob
    job_minute = job.run_repeating(water_job, interval=60, first=0)

    updater.start_polling()
    updater.idle()
