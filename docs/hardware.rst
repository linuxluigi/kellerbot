.. _hardware:

Hardware
========

Für dieses Projekt wurde ein `Raspberry Pi Model B+ V1.2`, 2 `Arduino Nano`, ein `DHT22 temperature-humidity sensor`,
2 `zwei ardriges nicht abgeschirmtes Kupferkabel` und ein `TP-LINK WLAN Router` verwendet.

Raspberry Pi
------------

Um den `DHT22 temperature-humidity sensor` ansteuern zu können oder für den :ref:`aufbau_1_raspberry_pi_gpio`
wird ein Raspberry Pi oder ein ähnlicher Einplatinenrechner mit GPIO benötigt.

DHT22 Temperatur- & Luftfeuchtigkeitssensor
-------------------------------------------

Der ``DHT22 Temperatursensor und Luftfeuchtigkeitssensor`` ist für dieses Projekt ein Modell welches mit Platine
ausgeliefert wurde und ist daher wärend des ansteckens mit dem Raspberry Pi unterschiedlich gegenüber Modellen ohne
Platine.

Arduino Nano
------------

Für dieses Projekt wurden nicht Orginale `Arduino Nanos` verwendet, dadurch müssen die entsprechenden Treiber noch
nach installiert werden. Die Treiber sollten aber nur dann nachinstalliert werden, wenn diese nicht schon vom Werk aus
auf dem System vorhanden sind, wie z.B. MacOs.

Auf der Rückseite des Nanos (:numref:`Arduino_Nano_Controller`) steht der Controller Name.

.. _Arduino_Nano_Controller:
.. figure:: _static/arduino-nano-controller.jpg
    :align: center
    :scale: 12%
    :alt: Arduino Nano

    Arduino Nano Controller Name

In diesen Fall ist der Treiber auf https://sparks.gogo.co.nz/ch340.html zu finden.

2 ardriges nicht abgeschirmtes Kupferkabel
------------------------------------------

Die Kabel werden für die Kapazitätsmessung benötigt. Mithilfe der Kapazitätsmessung ist es dann möglich 4 verschiedene
Zustände des Kabels zu messen, mitunter ob das Kabel unter Wasser ist. Wichtig bei dem Kabel ist es, das die beiden
Kabelstränge direkt nebeneinander sind wie bei ein Telefonkabel oder Lautsprecherkabel.


.. todo Kabelbilder einfügen

TP-LINK WLAN Router
-------------------

Der `TP-LINK WLAN Router` ist Optional, er dient außschlich als WLAN Repeater um den Raspberry Pi über eine große
Distanz from WLAN Access Point. Dabei wird der Router mit dem Quelloffenden Betriebsystem openWrt geflasht womit er auch
als WLAN Repeater verwendet werden kann.

.. todo router einfügen