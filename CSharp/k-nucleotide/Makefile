THIS_FILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

compile:
	cp knucleotide.csharpcore-6.csharpcore Program.cs
	/usr/bin/dotnet build -c Release

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt" CSharp k-nucleotide

run:
	/usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

mem:
	/usr/bin/time -v /usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 0 < ${THIS_FILE_DIR}/../../knucleotide-input25000000.txt
