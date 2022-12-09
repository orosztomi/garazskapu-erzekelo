# garazskapu-erzekelo
Garázskapu ultrahangos érzékelő: nyitva/zárva, Raspberry PI eszközön

A probléma: garázsban áll az autóm és a házunkkal szemben egy Posta található, ahol sok ember megfordul. Néhány autó kulcsa, amikor a tulajdonosa lezárja vagy kinyitja az autóját az nyitja a garázs ajtómat. Jellemzően a Koreai autók: Hyundai, Kia de egyéb márkák is. Valószínű, hogy azonos hullámhosszt használ az autó távirányítója és a garázs távirányítója. A garázs ajtó állapotának monitorozására találtam ki ezt a programot, ami egy ultrahangos távolságmérő szenzoron alapul és ha a garázsajtó nyitva van, ami a program nyelvén azt jelenti, hogy az érzékelő előtt 10 cm-nél nagyobb távolságra található a garázsajtó akkor nyitva jelzést ad vissza, ellenkező esetben zárva.

Eszközszükséglet:
	Raspberry PI 4
	Breadboard
	4 jumper kábel
	Ultrasonic sensor: HC-SR04
![image](https://user-images.githubusercontent.com/93983032/206804016-4561e9d6-6898-44b5-b5ac-ff9178e57e1a.png)
