compile:
	cp binarytrees.java-7.java binarytrees.java
	${JAVA_HOME_1_8}/bin/javac -d .  binarytrees.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_1_8}/bin/java binarytrees 21" Java binary-trees

run:
	${JAVA_HOME_1_8}/bin/java binarytrees 21

mem:
	/usr/bin/time -v${JAVA_HOME_1_8}/bin/ java binarytrees 21

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_1_8}/bin/java binarytrees 21
