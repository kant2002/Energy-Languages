compile:


xmeasure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 pidigits.yarv-5.yarv 10000" Ruby pidigits

run:
	${RUBY_HOME}/ruby -W0 pidigits.yarv-5.yarv 10000

mem:
	/usr/bin/time -v  ${RUBY_HOME}/ruby -W0 pidigits.yarv-5.yarv 10000

valgrind:
	valgrind --tool=massif --stacks=yes  ${RUBY_HOME}/ruby -W0 pidigits.yarv-5.yarv 10000
