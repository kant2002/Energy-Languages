compile:
	#${JAVA_HOME_20_0}/bin/javac -d . -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide.java
	#${JAVA_HOME_20_0}/bin/javac -d . knucleotide.java

measure:
	#sudo modprobe msr
	#sudo ../../RAPL/main "${JAVA_HOME_20_0}/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < knucleotide-input25000000.txt" Java k-nucleotide

run:
	#${JAVA_HOME_20_0}/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < knucleotide-input25000000.txt

mem:
	#/usr/bin/time -v  ${JAVA_HOME_20_0}/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < knucleotide-input25000000.txt

valgrind:
	#valgrind --tool=massif --stacks=yes  ${JAVA_HOME_20_0}/bin/java  -cp .:/usr/local/src/java-libs/fastutil-7.0.12.jar knucleotide 0 < knucleotide-input25000000.txt
