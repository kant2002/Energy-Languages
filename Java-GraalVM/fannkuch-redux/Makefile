compile:
	${JAVA_HOME_20_0}/bin/javac -d  .  fannkuchredux.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_20_0}/bin/java   fannkuchredux 12" Java fannkuch-redux

run:
	${JAVA_HOME_20_0}/bin/java   fannkuchredux 12

mem:
	/usr/bin/time -v  ${JAVA_HOME_20_0}/bin/java   fannkuchredux 12

valgrind:
	valgrind --tool=massif --stacks=yes  ${JAVA_HOME_20_0}/bin/java   fannkuchredux 12
