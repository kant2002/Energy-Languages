compile:
	cp fasta.java-5.java fasta.java
	${JAVA_HOME_21_0}/bin/javac -d . fasta.java
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JAVA_HOME_21_0}/bin/java   fasta 25000000" Java fasta

run:
	${JAVA_HOME_21_0}/bin/java   fasta 25000000

mem:
	/usr/bin/time -v ${JAVA_HOME_21_0}/bin/java   fasta 25000000

valgrind:
	valgrind --tool=massif --stacks=yes ${JAVA_HOME_21_0}/bin/java   fasta 25000000
