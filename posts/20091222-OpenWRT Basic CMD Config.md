##OpenWRT basic command line configuration {:.blog-post-title}

December 22, 2009
{:.blog-post-meta}



OpenWRT is an open source third party firmware, originally built for the Linksys WRT54G.  Support has been expand to include networking devices ranging from consumer to enterprises  grade routers and wireless access points. OpenWRT has a variety of web based user interfaces, as you would expect with any networked device, but because the operating system is based on the Linux kernel, the command line is where its flexibility really shows.

If you are familiar with any *inx operating system, you will find working and navigating in Dropbear, OpenWRT's terminal, simple.  The binary I will be focusing on is uci or Unified Configuration Interface.  As its name implies, uci is the program responsible for making all configuration changes to system files located /etc/config/.


The syntax is broken into three parts.  The first two are mandatory with the [arguments] field being optional depending on the [option]


`uci options commands arguments`


[commands] is also broken down into three parts: file.section.option.  Section can be called by their name, such as lan, wan as in /etc/config/network or wifi0 in /etc/config/wireless.  Sections that do not have names can be called their position in the array of sections.  An example of this is wireless.@wifi-iface[0].ssid


To view a configuration file such as /etc/config/network:

`uci export network`


Making or adding a new value to a section, in this case the default gatway, is easy as typing:


`uci set network.lan.gateway=10.168.1.1`

OR

`uci set network.@interface[1].gateway=10.168.1.1`

To add  and delete options use uci add or uci delete:

`uci delete wireless.@wifi-iface[0].encryption`

It is also possible to set DHCP options, such as the gateway or DNS servers to push to clients. Refer to this <http://www.networksorcery.com/enp/protocol/bootp/options.htm">website> to find the DHCP option codes.

`uci add_list network.lan.dhcp_option="3,10.168.1.1"`


When done making changes you must run:

`uci commit [configuration]`

example: `uci commit network`


It is possible to change the behavior of startup services.

```
root@OpenWRT:~#/etc/init.d/network
Syntax /etc/init.d/network [command]
Available commands:
start      Start the service
stop      Stop the service
restart   Restart the service
reload    Reload configuration files (or restart if that fails)
enable   Enable service autostart
disable    Disable service autostart
```


**Script**

OpenWRT does not try to set the correct time and date at startup.  It is possible to install an NTP (Network Time Protocol) client that will run as a daemon, but I chose to write a script utilizing the already built-in rdate to configure the date and time.


1) Set the your timezone. Refer to this <http://docs.sun.com/source/816-5523-10/appf.htm> from sun.com for a list of timezone codes

``` 
uci set system.@system[0].timezone=CST6CDT
uci commit system 
```


2) [Download](http://alex.hrck.net/docs/set_date.sh) (or copy and paste) the set_date.sh script to /etc/init.d/setdate on the device running OpenWRT.

```
#!/bin/sh /etc/rc.common
START=10
start() {
DATE="1969"
while [ $DATE = "1969" ]; do
        /usr/sbin/rdate 128.138.140.44
        if [ $? -eq 1 ]; then
                sleep 60
        fi
        DATE=`date +%Y`
done
exit 0 
```


3) change mode and enable the script to run at boot

``` 
chmod +x /etc/init.d/setdate
/etc/init.d/setdate enable 
```


4) Reboot the device and check the date.

``` 
# date
Mon Dec 28 11:36:28 CST 2009 
```
