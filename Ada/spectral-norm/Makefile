compile:
	gnatchop -r -w spectralnorm.gnat-4.gnat
	gnatmake -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp -f spectralnorm.adb -o spectralnorm.gnat-4.gnat_run 
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectralnorm.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division.ads
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-d.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp division-s.ads
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-d.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-dist.adb
	gcc-13 -c -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -gnatNp spectral_utils-s.adb
	gnatbind-13 -x spectralnorm.ali
	gnatlink-13 spectralnorm.ali -O3 -fomit-frame-pointer -march=native -msse3 -mfpmath=sse -o spectralnorm.gnat-4.gnat_run

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "./spectralnorm.gnat-4.gnat_run 5500" Ada spectral-norm

run:
	./spectralnorm.gnat-4.gnat_run 5500

mem:
	/usr/bin/time -v ./spectralnorm.gnat-4.gnat_run 5500

valgrind:
	valgrind --tool=massif --stacks=yes ./spectralnorm.gnat-4.gnat_run 5500	
