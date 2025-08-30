compile:
	cp mandelbrot.java-2.java mandelbrot.java
	${JAVA_HOME_20_0}/bin/javac -d .  mandelbrot.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_20_0}/bin/java   mandelbrot 16000" Java mandelbrot

run:
	${JAVA_HOME_20_0}/bin/java   mandelbrot 16000

mem:
	/usr/bin/time -v ${JAVA_HOME_20_0}/bin/java   mandelbrot 16000

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_20_0}/bin/java   mandelbrot 16000
