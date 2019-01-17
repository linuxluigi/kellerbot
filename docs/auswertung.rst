Projekt Auswertung
==================

Genauigkeit & Stabilität
------------------------

In den Tests, in denen hauptsächlich die Kabelenden mit Wasser in Berührung kamen, funktionierten die Tests zuverlässig und
innerhalb von 2 Sekunden wurden die Zustandsänderungen via Telegram gesendet. Es fehlte zum Schluss leider die Zeit für
ausführlichere Tests. So wäre es interessant zu sehen, wie sich die Kapazität im Kabel ändert, wenn das Kabel zu Teilen
in Wasser wäre, ohne dass die Kabelenden direkt mit Wasser in Kontakt kommen oder wie sich die Kapazität in den Kabeln
ändert, wenn der Keller eine sehr hohe Luftfeuchtigkeit hat.

Der :ref:`aufbau_1_raspberry_pi_gpio` war über einen Monat im Keller in Betrieb. Bei diesem ersten Aufbau war die
Netzwerk Anbindung über einen WLAN Stick geregelt. Dieser hatte zwar eine relativ starke Sende- & Empfangsleistung, aber die
Reaktionszeit des :term:`Raspberry Pi`'s war durch WLAN Abbrüche gemindert und dauerte des Öfteren über einige Minuten.
Außerdem wurden im ersten Aufbau die Kabel nur alle 3 Minuten auf Wasser überprüft, so dass fließendes Wasser nicht
immer als solches gemessen werden konnte. Trotz den Problemen mit dem Aufbau, war der :term:`Raspberry Pi` die gesamte
Zeit zuverlässig über den Telegram Bot erreichbar.

Der :ref:`aufbau_2` überzeugte hingegen mit der schnellen Reaktionszeit auf kurzzeitige Änderungen. Auch der Austausch
des WLAN Sticks zu einen WLAN Router als :term:`WLAN zu LAN Bridge` sorgte für eine schnelle Reaktionszeit des
Telegram Bots. Der Aufbau steht nun seit zwei Wochen im Keller & arbeitet dabei fehlerfrei. Auch die Arduinos arbeiten
im Dauerbetrieb, auch bislang fehlerfrei und senden innerhalb von Sekunden Zustandsänderungen an den :term:`Raspberry Pi`.

Stromverbrauch
--------------

Der :term:`Raspberry Pi` verbraucht ohne angeschlossene USB Geräte, mit Ethernet Anbindung und aktivem KellerBot Daemon
1,5 Watt pro Stunde. Mit jedem neu angeschlossenen :term:`Arduino Nano` steigt der Verbrauch um 0,2 Watt die Stunde.
So ergab es bei meinen Aufbau mit 2 angeschlossenden :term:`Arduino Nanos` ein gesamt Verbrauch von 1,9 Watt pro Stunde,
Stromverbauch ist auf :numref:`stromverbauch` zu sehen. Bei durchschnittlichen 720 Stunden im Monat ergibt sich ein
Monatsverbauch von 1,368 Kilowatt.

.. _stromverbauch:
.. figure:: _static/fotos/IMG_20190110_132722.jpg
    :align: center
    :scale: 6%
    :alt: Stromverbauch des Aufbaus mit 2 Arduinos, Anzeige in Watt pro Stunde

    Stromverbauch des Aufbaus mit 2 Arduinos, Anzeige in Watt pro Stunde

Fazit
-----

Das angestrebte Ziel wurde kosteneffektiv gelöst, wobei nur 3 :term:`Arduino Nanos` für ca 13€ nachgekauft werden mussten.
Die restlichen Kabel & Hardware stammten aus alten Projekten und wurden nicht mehr verwendet. Auch können nun alle
Bewohner des Hauses zeitnah einen Wasserschaden in Keller frühzeitig bemerken, wobei größere Schäden vermieden werden können.

Telegram überraschte mich bei der Arbeit äußert positiv. Einen eigenen Bot mittels Telegram zu erstellen stellte sich
als sehr einfach dar. Auch ist es ein starker Vorteil, dass keine extra Software auf dem Smartphone installiert werden muss,
um den KellerBot zu verwenden. Durch die leichte Bedienung ist Telegram auch ein praktisches Tool für Computer-Leihen:
Sie müssen sich nicht erst an eine neue Software gewöhnen, sondern erhalten im Erstfall einfach zuverlässig eine
Nachricht auf ihr Smartphone.