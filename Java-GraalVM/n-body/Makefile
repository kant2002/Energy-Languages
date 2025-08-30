compile:
	cp nbody.java-4.java nbody.java
	${JAVA_HOME_20_0}/bin/javac -d .  nbody.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_20_0}/bin/java   nbody 50000000" Java n-body

run:
	${JAVA_HOME_20_0}/bin/java   nbody 50000000

mem:
	/usr/bin/time -v ${JAVA_HOME_20_0}/bin/java   nbody 50000000

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_20_0}/bin/java   nbody 50000000
