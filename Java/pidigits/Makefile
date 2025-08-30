compile:
	cp pidigits.java-2.java pidigits.java
	${JAVA_HOME_1_8}/bin/javac -d .  pidigits.java
xmeasure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_1_8}/bin/java -Djava.library.path=Include/java  pidigits 10000" Java pidigits

run:
	${JAVA_HOME_1_8}/bin/java -Djava.library.path=Include/java  pidigits 10000

mem:
	/usr/bin/time -v ${JAVA_HOME_1_8}/bin/java -Djava.library.path=Include/java  pidigits 10000

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_1_8}/bin/java -Djava.library.path=Include/java  pidigits 10000

