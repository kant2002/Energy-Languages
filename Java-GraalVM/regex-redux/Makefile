compile:
	cp regexredux.java-3.java regexredux.java
	${JAVA_HOME_20_0}/bin/javac -d .  regexredux.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_20_0}/bin/java   regexredux 0 < ../../regexredux-input5000000.txt" Java regex-redux

run:
	${JAVA_HOME_20_0}/bin/java   regexredux 0 < ../../regexredux-input5000000.txt

mem:
	/usr/bin/time -v ${JAVA_HOME_20_0}/bin/java   regexredux 0 < ../../regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_20_0}/bin/java   regexredux 0 < ../../regexredux-input5000000.txt
