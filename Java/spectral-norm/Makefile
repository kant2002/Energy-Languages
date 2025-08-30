compile:
	cp spectralnorm.java-2.java spectralnorm.java
	${JAVA_HOME_1_8}/bin/javac -d .  spectralnorm.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "java   spectralnorm 5500" Java spectral-norm

run:
	${JAVA_HOME_1_8}/bin/java   spectralnorm 5500

mem:
	/usr/bin/time -v ${JAVA_HOME_1_8}/bin/java   spectralnorm 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_1_8}/bin/java   spectralnorm 5500
