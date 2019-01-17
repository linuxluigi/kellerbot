Theoretischer Aufbau
====================

Zu lösendes Problem
-------------------

Nachdem im letzten Jahr ein kleiner und größerer Wasserschaden im Keller bei uns aufkam und der große
Wasserschaden in der Ferienzeit durch zufall bemerkt wurde, überlegte ich mir, wie ein Warnmeldesystem aussehen könnte.
Problematisch war es auch bei den großen Wasserschaden, das dieser in der Ferienzeit war und gut und gerne ein paar Tage
unbemerkt bleiben hätte können. Also auch wenn nun der Keller längere Zeit nicht mehr betreten wird, sollte nun ein
Warnsystem installiert werden, wo ich auch die Erlaubnis der Hausverwaltung erhielt :)

Lösung
------

Grundkonzept
^^^^^^^^^^^^

Da im Keller eine Stromversorgung über eine Steckdoese sichergestellt werden konnte und auch das WLAN Signal aus der
Wohnetage im Keller ausreichend stark ist. Entschloss ich mich auf eine Simple :term:`Raspberry Pi` Lösung, wo die erfassenten
Sensor Daten über Telegram versendet werden sollten (:numref:`konzept_haus`).

.. _konzept_haus:
.. figure:: _static/haus.png
    :align: center
    :scale: 25%
    :alt: Grundkonzept des zu lösenden Problems

    Grundkonzept des zu lösenden Problems

Zusätzlich zur Wassermeldung sollte aber mittels eines :term:`DHT22 Temperatur- und Luftfeuchtigkeitssensor` die Luftfeuchtigkeit und
Temperatur auf abfrage gemessen werden.

.. _aufbau_1_raspberry_pi_gpio:

Aufbau 1: Raspberry Pi GPIO
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mein erster Ansatz war es über die :term:`GPIO` Schnittstelle des :term:`Raspberry Pi`'s zu messen ob an den Kabelenden ein Stromkreilauf
geschlossen wurde (in :numref:`konzept_raspberry_pi_version` Stromkreis schließen mittels Buttons dargestellt) oder nicht,
dafür war bis auf ein altes Telefonkabel und der :term:`Raspberry Pi` auch nichts weiter nötig. Welches den Versuch leicht
umsetztbar machte.

.. _konzept_raspberry_pi_version:
.. figure:: _static/TelegramBot_raspberry_pi_version_bb.png
    :align: center
    :scale: 30%
    :alt: Raspberry Pi :term:`GPIO` Lösung

    Raspberry Pi :term:`GPIO` Lösung

Wärend der Umsetzung des Versuches sind mehrere Probleme aufgetreten.


1. Es war in der Software nur möglich zu messen ob ein Stromkreislauf geschlossen wurde oder nicht, es war nicht möglich
   fest zu stellen ob das Kabel an den Enden kurzgeschlossen wurde oder ob gar kein Kabel vorhanden war.

2. Die Messung erfolgte in zu großen Abständen, somit war die Aussagekraft nicht immer zuverlässig.

3. Es gab nur eine berenzte Anzahl an Kabeln die am :term:`Raspberry Pi` angeschlossen werden konnten.


Der Code des Versuches kann im Branch `feature/raspberry-pi-gpio-sensor-mode`_ heruntergeladen werden.

.. _`feature/raspberry-pi-gpio-sensor-mode`: https://github.com/linuxluigi/kellerbot/tree/feature/raspberry-pi-gpio-sensor-mode

.. _aufbau_2:

Aufbau 2: Raspberry Pi und Arduino Nano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um die in :ref:`aufbau_1_raspberry_pi_gpio` beschriebenden Probleme zu lösen, bot sich eine Lösung mit :term:`Arduino Nanos` an,
die an den Kabeln eine Kapazitätsmessung durchführen, womit sich mehrere Zustände auslesen lassen.

- kein Kabel an den Pin's angeschlossen

- Kabel ist kurzgeschlossen

- Kabel liegt im trockenden

- Kabel liegt im Wasser

Zumal wird in diesem Aufbau fortlaufend das Kabel auf diese Zustände überprüft und kann somit in Echtzeit die Daten zu
Telegram senden.

Das dritte Problem kann durch ein aktiven USB Hub gelöst werden, der am :term:`Raspberry Pi` angeschlossen wird und an diesen
Hub können somit eine große Zahl von Arduinos ausgelesen werden.

Messung der Kapazität über ein Arduino
""""""""""""""""""""""""""""""""""""""

Während der Kapazitätsmessung wird die Zeitkonstante ``TC`` über ein Widerstandskondensator ``RC`` innerhalb des
Stromkreislaufes gemessen, wie lange die Kapazität ``C`` benötigt um 63.2% ihrer gesamten Spannung zu laden.


.. _Theorie-Kapazität:
.. figure:: _static/theorie-kapazitaet.png
    :align: center
    :scale: 60%
    :alt: Kapazitäts Messung

    Kapazitäts Messung

Größere Kapazitäten benötigen länger um zu laden, deshalb erhalten diese eine größere Zeitkonstante. Die Kapazität in einer
Widerstandskondensatorschaltung ist verbunden mit der Zeitkonstante mit der Formel:

.. math::

  Formel: TC = R \cdot C

- TC = Zeitkonstante in Sekunden
- R = Wiederstand in Ohm
- C = Kapazität in Fahrad

Durch Umstellung der Gleichung nach der Kapazität ergibt sich folgende Gleichung:


.. math::

  C\ =\ \frac{TC}{R}

Nach Messungen von http://www.circuitbasics.com/how-to-make-an-arduino-capacitance-meter/ kann der Arduino mit einer
Schaltung mit nur 2 Drähten (:numref:`Arduino_Nano_Schaltung` und :numref:`Arduino_Nano_Schaltung_Schem`) unbekannte
Kapazitäten zwischen 470 uF und 18 pF messen.

.. _Arduino_Nano_Schaltung:
.. figure:: _static/Arduino_bb.png
    :align: center
    :scale: 35%
    :alt: Arduino Nano Schaltung

    Arduino Nano Schaltung

.. _Arduino_Nano_Schaltung_Schem:
.. figure:: _static/Arduino_schem.png
    :align: center
    :scale: 35%
    :alt: :term:`Arduino Nano` Schaltung Schematische Darstellung

    :term:`Arduino Nano` Schaltung Schematische Darstellung

:cite:`arduino_|_44_how_2015`
:cite:`noauthor_arduino_nodate`

Problem: Internet im Keller
---------------------------

Da keine direkte Netzwerkverbindung von der Wohnung bis zum Keller führt und auch der WLAN Hotspot im 2.OG steht und
bis zum Keller 3 Etage überbrück werden müssen und dabei eine stabile Internetverbindung bestehen muss, gab es 2
Lösungsmöglichkeiten, wo ich keine neue Hardware kaufen musste.


Powerline
^^^^^^^^^

:term:`Powerline` ist ein Netzwerk über das Stromnetz, welches auch über mehrere Wohnungen verlegt werden kann. In meinen Test
konnte habe ich Geräte von 2 verschiedenen Anbieter ausprobiert, wobei beide die Distanz gemeistert haben, aber auch ein
erhöhtes Ausfallsrisiko. So das es innerhalb einer Woche Manuell neugestart werden muss, dadurch viel diese Möglichkeit
hier aus.

W-LAN
^^^^^

Um herauszufinden ob dieser Lösungsansatz möglich ist, schaute ich mir mittels der Android App `Wifi Analyzer`_
die Reichweite unserers 2.4 GHz WLAN's an und stellte fest, das im Keller ein geringes aber stabiles signal ankam.

.. _`Wifi Analyzer`: https://play.google.com/store/apps/details?id=com.farproc.wifi.analyzer&hl=en_US

Da mir für dieses Projekt ein USB WLAN Stick für den :term:`Raspberry Pi` fehlte, hatte ich ein alten TP-LINK Router genommen
und dort ein neues Betriebsystem openWrt_ aufgespielt. Somit konnte nun der WLAN Router nicht nur als Acces Point dienen
sondern auch sich in ein anderes WLAN signal einwählen und den Datenverkehr über Ethernet routen, er konnte nun also als
ein :term:`WLAN zu LAN Bridge` arbeiten (:numref:`haus_wlan_repeater`).

.. _openWrt: https://openwrt.org/

.. _haus_wlan_repeater:
.. figure:: _static/haus-WLAN-Repeater.png
    :align: center
    :scale: 30%
    :alt: WLAN zu LAN Bridge setup - Theorie

    :term:`WLAN zu LAN Bridge` setup - Theorie

Dieses Setup sorgt nun auch dafür, wenn die WLAN Verbindung abbricht z.B. durch ein Router neustart des :term:`Access Point`,
das sich der Brige Router von allein wieder neu verbindet. Ein weiterer nützlicher Nebeneffekt dieser Methode gegenüber
eines durchschinttliches WLAN Sticks ist es, das die Antennen des TP-Link Routers sehr Leistungsstark sind und sich
gut in Richtung des Signals ausrichten lassen (:numref:`haus_wlan_repeater_foto`).

.. _haus_wlan_repeater_foto:
.. figure:: _static/fotos/IMG_20190110_132558.jpg
    :align: center
    :scale: 8%
    :alt: WLAN zu LAN Bridge setup - Praxis

    WLAN zu LAN Bridge setup - Praxis