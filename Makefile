CC := sh /home/ning/Android/Sdk/ndk/22.0.7026061/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android21-clang

objs := fr.o	\
		util.o 	\
		vlist.o \
		



all: $(objs)
	$(CC) main.c $(objs) -o hello.out

%.o: %.c
	$(CC) -c -o $@ $<

.PHONY: clean
clean:
	@rm -f *.o *.out
