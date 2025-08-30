compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 binarytrees.yarv-5.yarv 21" Ruby binary-trees

run:
	${RUBY_HOME}/ruby -W0 binarytrees.yarv-5.yarv 21

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 binarytrees.yarv-5.yarv 21

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 binarytrees.yarv-5.yarv 21
