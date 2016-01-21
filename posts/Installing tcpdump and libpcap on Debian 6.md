##Installing tcpdump and libpcap on Debian 6 {:.blog-post-title}

January 15, 2012
{:.blog-post-meta}


I ran into an issue when trying to install the latest version of tcpdump (4.2.0) with libpcap (1.2.0) on Debain recently. The error during the build process of tcpdump and looked like:

	./print-ppi.c:16:17: error: ppi.h: No such file or directory
	./print-ppi.c: In function âppi_header_printâ:
	./print-ppi.c:23: error: expected â=â, â,â, â;â, âasmâ or â__attribute__â before â*â token
	./print-ppi.c:23: error: âhdrâ undeclared (first use in this function)
	...snip...
	make: *** [print-ppi.o] Error 1

To fix this issue I grabbed the ppi.h file from the tcpdump Github project and recompiled.

```
cd ./tcpdump-4.2.0
wget https://github.com/mcr/tcpdump/blob/master/ppi.h
./configure
make && make install
mv /usr/local/sbin/tcpdump /usr/sbin/tcpdump
```

Running `tcpdump --version` to verfiy the program was installed correctly.

A side note, remove the version of libpcap (0.8) that ships with Debian, otherwise tcpdump will complain during the build process. Simply apt-get remove libpcap0.8 then compile version 1.2.0 as normal.