.. _hardware:

Hardware
========

Für dieses Projekt wurde ein `Raspberry Pi Modell B+ V1.2`, 2 :term:`Arduino Nano`, ein :term:`DHT22 Temperatur- und Luftfeuchtigkeitssensor`,
2 `zwei ardriges nicht abgeschirmtes Kupferkabel` und ein `TP-LINK WLAN Router` verwendet.

Raspberry Pi
------------

Um den :term:`DHT22 Temperatur- und Luftfeuchtigkeitssensor` ansteuern zu können oder für den :ref:`aufbau_1_raspberry_pi_gpio`
wird ein :term:`Raspberry Pi` oder ein ähnlicher :term:`Einplatinenrechner` mit :term:`GPIO` benötigt.

DHT22 Temperatur- & Luftfeuchtigkeitssensor
-------------------------------------------

Der :term:`DHT22 Temperatur- und Luftfeuchtigkeitssensor` ist ein Sensor, der mit einer Platine
ausgeliefert wurde und daher anders mit dem :term:`Raspberry Pi` angeschlossen werden muss.

Arduino Nano
------------

Für dieses Projekt wurden nicht Orginale :term:`Arduino Nano` verwendet, sodurch die entsprechenden Treiber
nachinstalliert werden müssen. Die Treiber sollten aber nur dann nachinstalliert werden, wenn diese nicht schon vom Werk aus
auf dem System vorhanden sind, wie z.B. MacOs.

Auf der Rückseite des Nanos (:numref:`Arduino_Nano_Controller`) steht der Controller Name.

.. _Arduino_Nano_Controller:
.. figure:: _static/arduino-nano-controller.jpg
    :align: center
    :scale: 12%
    :alt: Arduino Nano

    :term:`Arduino Nano` Controller Name

In diesen Fall ist der Treiber auf https://sparks.gogo.co.nz/ch340.html zu finden.

2 ardriges nicht abgeschirmtes Kupferkabel
------------------------------------------

Die Kabel werden für die Kapazitätsmessung benötigt. Mit Hilfe der Kapazitätsmessung ist es dann möglich, 4 verschiedene
Zustände des Kabels zu messen, mitunter ob das Kabel unter Wasser ist. Wichtig bei dem Kabel ist es, dass die beiden
Kabelstränge direkt nebeneinander sind, wie bei ein Telefonkabel oder Lautsprecherkabel.


.. todo Kabelbilder einfügen

TP-LINK WLAN Router
-------------------

Der `TP-LINK WLAN Router` ist optional, er dient ausschließlich als :term:`WLAN zu LAN Bridge` um den :term:`Raspberry Pi`
über eine große Distanz zu dem :term:`WLAN Access Point`. Dabei wird der Router mit dem quelloffenen Betriebsystem
:term:`openWrt` aufgespielt, womit er auch als :term:`WLAN zu LAN Bridge` verwendet werden kann.

.. todo router einfügen