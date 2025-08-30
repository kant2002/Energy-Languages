compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 spectralnorm.yarv-5.yarv 5500" Ruby spectral-norm

run:
	${RUBY_HOME}/ruby -W0 spectralnorm.yarv-5.yarv 5500

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 spectralnorm.yarv-5.yarv 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 spectralnorm.yarv-5.yarv 5500

