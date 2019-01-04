.. These are the Travis-CI and Coveralls badges for your repository. Replace
    your *github_repository* and uncomment these lines by removing the leading two dots.

.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master

.. image:: https://readthedocs.org/projects/kellerbot/badge/?version=latest
    :target: https://kellerbot.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

``kellerBot`` ist ein Raspberry Pi & Arduino Projekt, welches anhand eines 2 ardigen Kabels misst, ob Wasser an den
Kabel enden ist, das Kabel kurzgeschlossen, das Kabel nicht angeschlossen oder ob das Kabel ohne geschlossenden
Stromkreis angeschlossen ist. Diese Daten werden von ein Telegram_ Bot in einer Chat Gruppe angezeigt.

.. _Telegram: https://telegram.org/

.. _project-logo:
.. figure:: _static/android-161184.png
    :align: center
    :scale: 20%
    :alt: Projekt Logo

    Projekt Logo, Quelle: https://pixabay.com/en/android-bot-robot-television-happy-161184/

Hardware
--------

* Raspberry Pi Model B+ V1.2
* DHT22 Temperatur- & Luftfeuchtigkeitssensor
* mehrere Arduinos Nanos + jeweils 2 ardige Kupferkabel

Befehle
--------

Telegrambot::

    hilfe - zeige alle Befehle an
    temperatur - Temeratur anzeigen
    luftfeuchtigkeit - Luftfeuchtigkeit anzeigen
    wassermelder - Wasser test

GPIO
----

GPIO - Layout
^^^^^^^^^^^^^

Die Dokumentation wurde für das ``Raspberry Pi Model B+ V1.2`` erstellt. Wenn ein anderen Raspberry Pi verwendet wird,
kann es sein das, dass GIPO Layout anders aussieht und der `DHT22` Sensor an anderen Pins angeschlossen werden muss.
Um das GPIO-Layout des Pi's herauszufinden, kann das Projekt https://github.com/RPi-Distro/python-gpiozero
genutzt werden :numref:`pinout`.

python-gpiozero installieren::

    sudo apt install python3-gpiozero # install
    pinout # run in cli

.. _pinout:
.. figure:: _static/pinout.png
    :align: center
    :scale: 35%
    :alt: pinout

    Pinout

Wenn du das ``Raspberry Pi Model B+ V1.2`` Modell verwendest, kannst du die gleichen Pins verwenden wie im Bild
(:numref:`raspberry_pi`) abgebildet.


.. _raspberry_pi:
.. figure:: _static/TelegramBot_bb.png
    :align: center
    :alt: Raspberry Pi

    Raspberry Pi Steckplan

DHT22 Temperatur- & Luftfeuchtigkeitssensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``+`` -> ``3V3``
* ``out`` -> ``GPIO 7``
* ``-`` -> ``GND``
