compile:
	cp fasta.fsharpcore Program.fs
	/usr/bin/dotnet build -c Release

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "/usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 25000000" FSharp fasta

run:
	/usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 25000000

mem:
	/usr/bin/time -v /usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 25000000

valgrind:
	valgrind --tool=massif --stacks=yes /usr/bin/dotnet ./bin/Release/net8.0/tmp.dll 25000000
