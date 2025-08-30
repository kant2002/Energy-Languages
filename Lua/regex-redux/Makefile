THIS_FILE_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

compile:

xmeasure:
	sudo modprobe msr
	sudo ../../RAPL/main "lua  regexredux.lua-2.lua 0 < ${THIS_FILE_DIR}/../../regexredux-input5000000.txt" Lua regex-redux

run:
	lua  regexredux.lua-2.lua 0 < ${THIS_FILE_DIR}/../../regexredux-input5000000.txt

mem:
	/usr/bin/time -v lua  regexredux.lua-2.lua 0 < ${THIS_FILE_DIR}/../../regexredux-input5000000.txt

valgrind:
	valgrind --tool=massif --stacks=yes lua  regexredux.lua-2.lua 0 < ${THIS_FILE_DIR}/../../regexredux-input5000000.txt
