THIS_FILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 knucleotide.yarv-7.yarv 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt" Ruby k-nucleotide

run:
	${RUBY_HOME}/ruby -W0 knucleotide.yarv-7.yarv 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 knucleotide.yarv-7.yarv 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 knucleotide.yarv-7.yarv 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt
