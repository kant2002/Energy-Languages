compile:
	cp pidigits.jruby pidigits.rb

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m pidigits.rb 10000" JRuby pidigits

run:
	${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m pidigits.rb 10000

mem:
	/usr/bin/time -v ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m pidigits.rb 10000

valgrind:
	valgrind --tool=massif --stacks=yes ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m pidigits.rb 10000 
