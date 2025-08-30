compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 fannkuchredux.yarv-2.yarv 12" Ruby fannkuch-redux

run:
	${RUBY_HOME}/ruby -W0 fannkuchredux.yarv-2.yarv 12

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 fannkuchredux.yarv-2.yarv 12

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 fannkuchredux.yarv-2.yarv 12
