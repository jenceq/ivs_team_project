#Sample Makefile
calc =
profile =
odevzdani = odevzdani
dokumentace = dokumentace.pdf
cesta_instalator_kalkulacky =
cesta_instalator_odchylky = 

all: run

run:
	@./..\$(calc).exe

profile:
	@./..\$(profile).exe

clean: 
	rd /S /Q __pycache__

test:
	@python math_lib_tests.py

pack: 
	mkdir ..\$(odevzdani)
	mkdir ..\$(odevzdani)\doc
	mkdir ..\$(odevzdani)\install
	mkdir ..\$(odevzdani)\repo

	xcopy ..\$(dokumentace) ..\$(odevzdani)\doc

	xcopy $(cesta_instalator_kalkulacky) ..\$(odevzdani)\install
	xcopy $(cesta_instalator_odchylky) ..\$(odevzdani)\install

	mkdir ..\$(odevzdani)\repo\plan
	mkdir ..\$(odevzdani)\repo\profiling
	mkdir ..\$(odevzdani)\repo\src

	xcopy ..\..\ivs_team_project ..\$(odevzdani)\repo
	xcopy ..\plan ..\$(odevzdani)\repo\plan
	xcopy ..\profiling ..\$(odevzdani)\repo\profiling
	xcopy ..\src ..\$(odevzdani)\repo\src

help:
	@echo napoveda