THIS_FILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

compile:
	cp knucleotide.hipe-3.hipe knucleotide.erl
	erlc +native +"{hipe, [o3]}" knucleotide.erl
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "erl -smp enable -noshell -run  knucleotide main 0 < ${THIS_FILE_DIR}/../../regexredux-input50000.txt" Erlang k-nucleotide

run:
	erl -smp enable -noshell -run  knucleotide main 0 < ${THIS_FILE_DIR}/../../regexredux-input50000.txt

mem:
	/usr/bin/time -v erl -smp enable -noshell -run  knucleotide main 0 < ${THIS_FILE_DIR}/../../regexredux-input50000.txt

valgrind:
	valgrind --tool=massif --stacks=yes erl -smp enable -noshell -run  knucleotide main 0 < ${THIS_FILE_DIR}/../../regexredux-input50000.txt
