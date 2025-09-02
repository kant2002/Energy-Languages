compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 nbody.yarv-2.yarv 50000000" Ruby n-body

run:
	${RUBY_HOME}/ruby -W0 nbody.yarv-2.yarv 50000000

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 nbody.yarv-2.yarv 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 nbody.yarv-2.yarv 50000000
