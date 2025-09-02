compile:
	cp spectralnorm.jruby-4.jruby spectralnorm.rb

measure:
	sudo modprobe msr
	sudo ../../RAPL/main "${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500" JRuby spectral-norm

run:
	${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500

mem:
	/usr/bin/time -v ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500

valgrind:
	valgrind --tool=massif --stacks=yes ${JRUBY_HOME}/ruby -Xcompile.fastest=true -Xcompile.invokedynamic=true -J-server -J-Xmn512m -J-Xms2048m -J-Xmx2048m spectralnorm.rb 5500
