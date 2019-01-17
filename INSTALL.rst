Installation
============

Vorbereitug
-----------

Für die Installation wird die :ref:`Hardware` und ein eingerichteter :ref:`Telegram` Bot benötigt.

Arduino
-------

Den ersten Arduino Nano an einen Computer anschließen und die Arduino IDE starten (falls diese noch nicht installiert ist,
kann diese via https://www.arduino.cc/en/Main/Software heruntergeladen werden).

Nach dem Starten den Inhalt der Datei ``arduino-capacitance-meter/arduino-capacitance-meter.ino`` in die Arduino Software
einfügen.

Die IDE für den Arduino Nano einstellen

Arduino Nano: ``Tools`` -> ``Board`` -> ``Arduino Nano``

Prozessor: ``Tools`` -> ``Processor`` -> ``ATmega328P (Old Bootloader)``

Port: ``Tools`` -> ``Port`` -> ``/dev/cu.wchusbserial14130`` (der Port kann von System zu System anders aussehen)

Nachdem die Einstellungen gesetzt wurden kann

Raspberry Pi
------------

DHT22 Temperatur- & Luftfeuchtigkeitssensor am Raspberry Pi anschließen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GPIO - Layout
"""""""""""""

Die Dokumentation wurde für das ``Raspberry Pi Model B+ V1.2`` erstellt. Wenn ein anderer Raspberry Pi verwendet wird,
kann es sein das, dass das :term:`GPIO` Layout anders aussieht und der `DHT22` Sensor an andere Pins angeschlossen werden muss.
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

Beim Verwenden des ``Raspberry Pi Model B+ V1.2`` Models, die gleichen Pins verwenden, wie im Bild
(:numref:`raspberry_pi`) abgebildet.

.. warning::
    Bei dem ``DHT22 Temperatursensor und Luftfeuchtigkeitssensor`` im Bild handelt es sich um ein Modell, welches
    mit Platine ausgeliefert wurde. Der Steckplan ohne Platine weicht von dieser Abbildung ab!

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

Für dieses Projekt wird eine saubere Raspbian Installation vorausgesetzt, die aktuelle Version kann von der offiziellen
Raspberry Pi Website heruntergeladen werden: https://www.raspberrypi.org/downloads/raspbian/

KellerBot Software
^^^^^^^^^^^^^^^^^^

KellerSensorTelegramBot kann auf dem Raspberry Pi über pip installiert werden::

    $ sudo pip3 install git+git://github.com/adafruit/Adafruit_Python_DHT.git
    $ sudo python3 -m pip install git+git://github.com/linuxluigi/kellerbot.git

Dieser Befehl lädt das Archiv und deren Abhänigkeiten aus dem Internet herunter und installiert diese.

Falls der Tarball heruntergeladen wurde, diesen entpacken und ausführen::

    $ sudo pip3 install git+git://github.com/adafruit/Adafruit_Python_DHT.git
    $ sudo python3 setup.py install

Nach der Installation des Pakets muss der Service geladen werden. Die Telegram Bot ID & Telegram Chat ID
(für die Telegram ID's siehe die Kaptiel :ref:`Telegram_create_bot_group` & :ref:`Telegram_create_bot`) in der service
konfig Datei eintragen und anschließend den Service neuladen. Automatisches Starten während des Bootvorgangs aktivieren
und den Service ausführen::

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

Als erstes die Arduinos via USB an den Raspberry Pi anschließen, dann den Pi mit einem WLAN Stick oder via
WLAN to Lan Bridge an das WLAN Netzwerk anschließen und alles mit Strom versorgen, wie in :numref:`hardware-anschluss`
dargestellt.

.. _hardware-anschluss:
.. figure:: _static/fotos/IMG_20190110_132558.jpg
    :align: center
    :scale: 5%
    :alt: Projekt Hardware Installation

    Projekt Hardware Installation

Die Kabel, die zur Messung dienen sollen, an einem Ende mit einem weiblichen Verbindungsstecker versehen und an die Pins
``A2`` & ``A1`` des jeweiligen Arduinos anstecken, wie in :numref:`hardware-arduino-anschluss` zu sehen.

.. _hardware-arduino-anschluss:
.. figure:: _static/fotos/IMG_20190110_132628.jpg
    :align: center
    :scale: 5%
    :alt: Arduino Kabelanschluss

    Arduino Kabelanschluss

Im letzten Schritt die Kabel, die an die Arduinos angeschlossen wurden, im Keller verlegen. Mindestens das Ende
muss am Boden liegen, um effektiv den Zustand messen zu können, wie in :numref:`hardware-kabel-verlegen-decke` und
:numref:`hardware-kabel-verlegen-ende` zu sehen.

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
    :alt: Messkabelende verlegen

    Messkabelende verlegen