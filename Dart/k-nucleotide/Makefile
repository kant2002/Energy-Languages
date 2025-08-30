THIS_FILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

compile:

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "dart  knucleotide.dart-2.dart 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt" Dart k-nucleotide

run:
	dart  knucleotide.dart-2.dart 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

mem:
	/usr/bin/time -v  dart  knucleotide.dart-2.dart 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes  dart  knucleotide.dart-2.dart 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt
