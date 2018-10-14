.. These are the Travis-CI and Coveralls badges for your repository. Replace
    your *github_repository* and uncomment these lines by removing the leading two dots.

.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master

.. image:: https://readthedocs.org/projects/kellerbot/badge/?version=latest
    :target: https://kellerbot.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

KellerBot is an Raspberry Pi project, where the sensor data are callable through a Telegram chat bot.

Hardware
--------

* Raspberry Pi Model B+ V1.2
* DHT22 temperature-humidity sensor
* 3 electric wire (for water detection)

Commands
--------

Telegrambot::

    help - zeige alle Befehle an
    temperature - Temeratur anzeigen
    humidity - Luftfeuchtigkeit anzeigen
    water - Wasser test

GPIO
----

GPIO - Layout
^^^^^^^^^^^^^

This documentation was design for the Raspberry Pi Model B+ V1.2. If you have a another pi you need the need to connect
the wire may differently. To find out the GPIO Layout for your own pi use https://github.com/RPi-Distro/python-gpiozero

Install python-gpiozero::

    sudo apt install python3-gpiozero # install
    pinout # run in cli

.. image:: _static/pinout.png
    :scale: 35%
    :alt: pinout

When you use the Raspberry Pi Model B+ V1.2 than you can use the same connections as in the picture below.

.. image:: _static/TelegramBot_bb.svg
    :alt: Raspberry Pi

DHT22 temperature-humidity sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``+`` -> ``3V3``
* ``out`` -> ``GPIO 7``
* ``-`` -> ``GND``

Water detection
^^^^^^^^^^^^^^^

* ``12`` + ``3V3`` or ``5V``
* ``16`` + ``3V3`` or ``5V``
* ``18`` + ``3V3`` or ``5V``






