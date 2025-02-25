
Dette projekt er et Tic Tac Toe-spil, hvor du kan spille mod en AI, som bruger minimax-algoritmen med alpha-beta pruning. Spillet kører i terminalen med farverige udskrifter, og det gemmer spillets bevægelser,
så du kan se en replay og følge din statistik (sejre, tab og uafgjorte kampe) over tid.


Funktioner:

AI med minimax og alpha-beta pruning:

AI’en vælger det bedste træk ved at evaluere alle mulige scenarier med en optimeret minimax-algoritme, der bruger alpha-beta pruning.

Tekstbaseret GUI:
Spillet kører i terminalen og bruger ANSI escape-sekvenser til at vise farver (blå for “X”, rød for “O”, sort for ledige celler og pink for gitterlinjer).


Scoreboard og statistik:

Hold styr på dine sejre, tab og uafgjorte kampe, som vises efter hver spilrunde.

Historik og replay

Spillets bevægelser gemmes, og efter spillet kan du vælge at afspille en replay, der viser hvert træk med en kort pause imellem.


Installation:

Klon repository

git clone https://github.com/din-bruger/TicTacToe.git
cd TicTacToe


Afhængigheder:

Dette projekt kræver ingen ekstra Python-biblioteker ud over standardbiblioteket. Sørg for at have Python 3 installeret.

Brug:
	1.	Kør spillet:
python tic_tac_toe.py


Spil:

Vælg dit symbol (“X” eller “O”) når du bliver bedt om det.

Spillet vælger tilfældigt, om du eller AI’en starter.

Indtast dit træk ved at skrive et tal mellem 1 og 9, som svarer til feltets position på brættet.

Efter spillet vises din statistik, og du får mulighed for at se en replay af spillet.

Du kan vælge at spille igen eller afslutte programmet.

 
