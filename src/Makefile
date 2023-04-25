#Sample Makefile
calc = gui.py
odchylka = stddev.py
odevzdani = xlazek01
dokumentace = ..\dokumentace.pdf
doxygen = ..\doxygen
manual = ..\manual.txt
instalator_kalkulacky = ..\setupKalcoolacka.exe
instalator_profiling = ..\setupStddev.exe

all: run

run:
	@python3.10 $(calc)

profile:
	@python3.10 $(odchylka) < ..\profiling\test_1000.txt

clean: 
	rd /S /Q __pycache__

test:
	@python math_lib_tests.py

pack: 
	mkdir ..\$(odevzdani)
	mkdir ..\$(odevzdani)\doc
	mkdir ..\$(odevzdani)\doc\doxygen
	mkdir ..\$(odevzdani)\install
	mkdir ..\$(odevzdani)\repo

	xcopy $(doxygen) ..\$(odevzdani)\doc\doxygen

	xcopy $(instalator_kalkulacky) ..\$(odevzdani)\install
	xcopy $(instalator_profiling) ..\$(odevzdani)\install

	mkdir ..\$(odevzdani)\repo\plan
	mkdir ..\$(odevzdani)\repo\profiling
	mkdir ..\$(odevzdani)\repo\src
	mkdir ..\$(odevzdani)\repo\mockup
	mkdir ..\$(odevzdani)\repo\.git

	xcopy /h /E ..\.git ..\$(odevzdani)\repo\.git
	xcopy ..\..\ivs_team_project ..\$(odevzdani)\repo
	xcopy ..\plan ..\$(odevzdani)\repo\plan
	xcopy ..\profiling ..\$(odevzdani)\repo\profiling
	xcopy ..\src ..\$(odevzdani)\repo\src
	xcopy ..\mockup ..\$(odevzdani)\repo\mockup

help:
	@echo **************
	@echo ** Napoveda **
	@echo **************
	@echo Do kalkulacky lze cisla zadavat primo pomoci klavesnice nebo pomoci tlacitek na obrazovce.
	@echo Pokud chcete vysledek smazat, musite hodnotu prvne nakliknout ve vystupnim okne nebo v zadavacim okne.
	@echo Funkce tlacitek :
	@echo ,
	@echo 	desetinna carka
	@echo C
	@echo 	smaze obsah vystupniho a zadavaciho okna.
	@echo DEL
	@echo 	maze posledni zadane cislo.
	@echo /
	@echo 	vydeli prvni zadane cislo druhym zadanym cislem.
	@echo x
	@echo 	vynasobi dve zadana cisla
	@echo -
	@echo 	odecte od prvniho cisla druhe cislo
	@echo +
	@echo 	secte dve zadana cisla
	@echo P
	@echo 	overi zda je zadane cislo prvocislo
	@echo ^
	@echo 	umocni cislo x(1. cislo) na mocninu cisla n(2. cislo)
	@echo !
	@echo 	faktorial cisla
	@echo odmocnina
	@echo 	provede n-tou odmocninu(cislo pred odmocninou) z x(cislo za odmocninou)
	@echo x na 2
	@echo 	umocni cislo na druhou
	@echo ?
	@echo 	otevre napovedu