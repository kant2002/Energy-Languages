compile:
	gnatchop -r -w fasta.gnat-5.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f fasta.adb -o fasta.gnat-5.gnat_run 
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp fasta.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence.ads
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence-creation.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp sequence-data.ads
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp lcg_random.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp line_io.adb
	gnatbind-13 -x fasta.ali
	gnatlink-13 fasta.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o fasta.gnat-5.gnat_run

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "./fasta.gnat-5.gnat_run 25000000" Ada fasta

run:
	./fasta.gnat-5.gnat_run 25000000

mem:
	/usr/bin/time -v ./fasta.gnat-5.gnat_run 25000000

valgrind:
	valgrind --tool=massif --stacks=yes ./fasta.gnat-5.gnat_run 25000000
