.. These are the Travis-CI and Coveralls badges for your repository. Replace
    your *github_repository* and uncomment these lines by removing the leading two dots.

.. .. image:: https://travis-ci.org/*github_repository*.svg?branch=master
    :target: https://travis-ci.org/*github_repository*

.. .. image:: https://coveralls.io/repos/github/*github_repository*/badge.svg?branch=master
    :target: https://coveralls.io/github/*github_repository*?branch=master

.. .. image:: https://readthedocs.org/projects/kellerbot/badge/?version=latest
    :target: https://kellerbot.readthedocs.io/de/latest/?badge=latest
    :alt: Documentation Status

- Online Dokumentation: https://kellerbot.readthedocs.io/de
- Quellcode: https://github.com/linuxluigi/kellerbot

``kellerBot`` ist ein Raspberry Pi & Arduino Projekt, welches anhand eines 2 ardigen Kabels misst, ob Wasser an den
Kabel enden ist, das Kabel kurzgeschlossen, das Kabel nicht angeschlossen oder ob das Kabel ohne geschlossenden
Stromkreis angeschlossen ist. Diese Daten werden von ein Telegram_ Bot in einer Chat Gruppe angezeigt.

Die :numref:`project-logo` ist das Projekt Logo, welches als Avatar für den Telegram Bot verwendet wird.

.. _Telegram: https://telegram.org/

.. _project-logo:
.. figure:: _static/android-161184.png
    :align: center
    :scale: 5%
    :alt: Projekt Logo

    Projekt Logo, Quelle: https://pixabay.com/en/android-bot-robot-television-happy-161184/

**Hardware**

Im der :numref:`projekt-aufbau` ist der komplette Aufbau zu sehen.

* Raspberry Pi Model B+ V1.2
* DHT22 Temperatur- & Luftfeuchtigkeitssensor
* mehrere Arduinos Nanos + jeweils 2 ardige Kupferkabel
* USB WLAN Dongel oder WLAN Repeater

.. _projekt-aufbau:
.. figure:: _static/fotos/IMG_20190110_132612.jpg
    :align: center
    :scale: 5%
    :alt: Projekt Aufbau

    Projekt Aufbau

**Telegram Bot Befehle**::

    hilfe - zeige alle Befehle an
    temperatur - Temeratur anzeigen
    luftfeuchtigkeit - Luftfeuchtigkeit anzeigen
    wassermelder - Wasser test
