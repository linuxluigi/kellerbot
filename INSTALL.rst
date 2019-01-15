Installation
============

Vorbereitug
-----------

Für die Installation wird die :ref:`Hardware` und ein eingerichteter :ref:`Telegram` Bot benötigt.

Arduino
-------

Den ersten Arduino Nano an ein Computer anschließen und die Arduino IDE starten (falls diese noch nicht installiert ist,
kann diese via https://www.arduino.cc/en/Main/Software heruntergeladen werden).

Nach den starten den Inhalt der Datei ``arduino-capacitance-meter/arduino-capacitance-meter.ino`` in der Arduino Software
einfügen.

Die IDE für den Arduino Nano einstellen

Arduino Nano: ``Tools`` -> ``Board`` -> ``Arduino Nano``

Prozessor: ``Tools`` -> ``Processor`` -> ``ATmega328P (Old Bootloader)``

Port: ``Tools`` -> ``Port`` -> ``/dev/cu.wchusbserial14130`` (der Port kann von System zu System anders aussehen)

Nachdem die Einstellungen gesetzte wurden kann

Raspberry Pi
------------

DHT22 Temperatur- & Luftfeuchtigkeitssensor am Raspberry Pi anschließen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GPIO - Layout
"""""""""""""

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

.. warning::
    Bei dem ``DHT22 Temperatursensor und Luftfeuchtigkeitssensor`` im Bild handelt es sich um ein Modell welches
    mit Platine Plantine ausgeliefert wurde, der Steckplan ohne Plantine weicht von dieser Abbildung ab!

.. _raspberry_pi:
.. figure:: _static/TelegramBot_bb.png
    :align: center
    :scale: 45%
    :alt: Raspberry Pi

    Raspberry Pi Steckplan

**DHT22 Temperatur- & Luftfeuchtigkeitssensor**

* ``+`` -> ``3V3``
* ``out`` -> ``GPIO 7``
* ``-`` -> ``GND``

Betriebsystem
^^^^^^^^^^^^^

Für dieses Projekt wird eine saubere Raspbian Installation vorausgesetzt, die aktuelle Version kann von der Offiziellen
Raspberry Pi Website heruntergeladen werden: https://www.raspberrypi.org/downloads/raspbian/

KellerBot Software
^^^^^^^^^^^^^^^^^^

KellerSensorTelegramBot kann auf den Raspberry Pi über pip installiert werden::

    $ sudo pip3 install git+git://github.com/adafruit/Adafruit_Python_DHT.git
    $ sudo python3 -m pip install git+git://github.com/linuxluigi/kellerbot.git

Dieser Befehl lädt das Archive und deren Abhänigkeiten aus dem Internet und instaliert diese.

Wenn der Tarball heruntergeladen wurde, entpacke diese und für diesen aus::

    $ sudo pip3 install git+git://github.com/adafruit/Adafruit_Python_DHT.git
    $ sudo python3 setup.py install

Nach dem Installation aktiviere starten nach dem booten und setze die Telegram Bot ID & Telegram Chat ID
(für die Telegram ID's sihe die Kaptiel :ref:`Telegram_create_bot_group` & :ref:`Telegram_create_bot`::

    $ sudo systemctl daemon-reload
    $ sudo systemctl edit keller.service

    [Service]
    Environment="BOT_ID=XXX"
    Environment="CHAT_ID=XXX"

    $ sudo systemctl daemon-reload
    $ sudo systemctl enable keller.service
    $ sudo systemctl start keller.service
    $ sudo systemctl status keller.service

Keller Hardware Installation
----------------------------

Nachdem auf die Arduinos das Script augespielt, an den Raspberry Pi der DHT22 Sensor angeschlossen und
Raspbian aufgespielt wurde, können die Komponenten im Keller installiert werden.

Als erstes die Arduinos via USB an den Raspberry Pi anschließen, dann den Pi mit ein WLAN Dongel oder via WLAN repeater
mit an das WLAN Netzwerk anschließen und alles mit Strom versorgen wie in :numref:`hardware-anschluss` dargestellt ist.

.. _hardware-anschluss:
.. figure:: _static/fotos/IMG_20190110_132558.jpg
    :align: center
    :scale: 5%
    :alt: Projekt Hardware Installation

    Projekt Hardware Installation

Die Kabel welches zur Messung dienen soll an ein Ende Weiblich Verbindungsstecker aufsetzten und diese an den Pins
``A2`` & ``A1`` des jeweiligen Arduinos aufsetzten, wie in :numref:`hardware-arduino-anschluss` zu sehen ist.

.. _hardware-arduino-anschluss:
.. figure:: _static/fotos/IMG_20190110_132628.jpg
    :align: center
    :scale: 5%
    :alt: Arduino Kabel Anschluss

    Arduino Kabel Anschluss

Im letzten Schritt die Kabel, welche an den Arduinos angeschlossen wurden, im Keller verlegen, so das mindestens das Ende
am Boden liegt um so effektive den Zustand messen zu können. Wie in :numref:`hardware-kabel-verlegen-decke` und
:numref:`hardware-kabel-verlegen-ende` zu sehen ist.

.. _hardware-kabel-verlegen-decke:
.. figure:: _static/fotos/IMG_20190110_132904.jpg
    :align: center
    :scale: 5%
    :alt: Messkabel verlegen an der Decke

    Messkabel verlegen an der Decke

.. _hardware-kabel-verlegen-ende:
.. figure:: _static/fotos/IMG_20190110_132911.jpg
    :align: center
    :scale: 5%
    :alt: Messkabel ende verlegen

    Messkabel ende verlegen