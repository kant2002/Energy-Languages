compile:


measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${RUBY_HOME}/ruby -W0 mandelbrot.yarv-5.yarv 16000" Ruby mandelbrot

run:
	${RUBY_HOME}/ruby -W0 mandelbrot.yarv-5.yarv 16000

mem:
	/usr/bin/time -v ${RUBY_HOME}/ruby -W0 mandelbrot.yarv-5.yarv 16000

valgrind:
	valgrind --tool=massif --stacks=yes ${RUBY_HOME}/ruby -W0 mandelbrot.yarv-5.yarv 16000
