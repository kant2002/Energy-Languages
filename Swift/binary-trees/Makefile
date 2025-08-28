compile:
	swiftc binarytrees.swift-9.swift -Ounchecked -whole-module-optimization -I/usr/local/opt/apr/include/apr-1 -lapr-1 -L/usr/local/opt/apr/lib -o binarytrees.swift-9.swift_run

xmeasure:
	sudo modprobe msr
	sudo ../../RAPL/main "./binarytrees.swift-9.swift_run 21" Swift binary-trees

run:
	./binarytrees.swift-9.swift_run 21

mem:
	/usr/bin/time -v ./binarytrees.swift-9.swift_run 21

valgrind:
	valgrind --tool=massif --stacks=yes ./binarytrees.swift-9.swift_run 21
