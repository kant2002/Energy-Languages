compile:

	cp fannkuchredux.jruby-2.jruby fannkuchredux.rb

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m fannkuchredux.rb 12" JRuby fannkuch-redux

run:
	${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m fannkuchredux.rb 12

mem:
	/usr/bin/time -v ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m fannkuchredux.rb 12

valgrind:
	valgrind --tool=massif --stacks=yes ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m fannkuchredux.rb 12
