##Jasager, Karma on the Fon {:.blog-post-title}

December 06, 2009
{:.blog-post-meta}


![Alt fon](/static/img/LaFonera_Hardware_LaFoneraPlus.jpg)

Karma is a set of tools for sniffing wireless network probe requests coming from wireless clients. Karma will automatically respond to any SSID probe and pretend to be the requested AP, giving the wireless client a good reason to connect.

Robin Wood (@digininja) took Karma to the next level by rebuilding it with the La Fonera routers, specifically the original Fon 2100 and the Fon+ 2201, in mind because of their low cost and small footprint. He also created a web interface for easy visualization of connected clients and to control functionality. He released this package as “Jasager, Karma on the Fon” in November 2008.

Fon+ 2201

Jasager comes in three different packages. First, Jasager also comes as a binary package, installable on a device that has an Atheros Wi-Fi card and already running OpenWRT.  Then is the official Jasager firmware, built, tested and hosted by Robin Wood on the projects homepage. Finally, Jasager has also been integrated into Piranha 2.0 alpha4 Firmware created by Orange (http://piranha.klashed.net/). Piranha 3.0 DOES NOT have Jasager integrated. I will be flashing my Fon+ with Piranha 2.0 alpha4 because of extra functionality Orange has built in, including a web interface for configuring the router.

As with most things in life, there are several ways to go about flashing a Fon with third party firmware. For simplicity, I will be using a GUI app called Fon Flash (http://www.gargoyle-router.com/download.php), but if you are interested in getting into the nitty gritty of flashing, check out the installation instructions on Jasager project page.

First you must flash the Fon with the firmware of your choice. I used Fon Flash and pointed it to the .squashfs rootfs file and the .lzma kernel file.
FonFlash

Fon Flash GUI

    Connect the Fon/+ through the LAN port to the NIC on your computer.
    Set the NIC’s IP address to 192.168.1.2 netmask 255.255.255.255.0 and gateway 192.168.1.1
    Press the “Flash router Now!” button on Fon Flash
    Reboot the Fon and you should see Fon Flash discover and connect to the router
    The .squashfs and .lzma files will be uploaded and installed. This process will take about 20 minutes. Be patient.
    The router will reboot and you will need to set your computer’s NIC to DHCP
    TELNET to 192.168.1.1:23
    To start the OpenSSH server you must set the root password with the command : passwd

TelnetFon

OpenWRT login message

For this setup, I will be using Jasager to bait wireless clients into using the Internet provided by my evil gateway:

    Remove wireless security, change the SSID, and change Fon’s IP

        vim /etc/config/wireless

        *note* Jasager firmware users change option disabled 1 to option disabled 0
        change option ssid default to option ssid ‘SOMETHING INTERESTING’
        *note* Piranha firmware users. remove option encryption psk2 and option key k4m1k4z3

        uci set network.lan.ipaddr=10.168.1.254 #set Fon's IP

        uci set network.lan.gateway=10.168.1.1 #set Fon's GW

        uci commit network

        Start Jasager on boot

            vim /etc/init.d/jasager

            make iwpriv ath0 karma 1 the last line of the start() function.
            Configure DHCP to provide a DNS server and an Evil gateway (our laptop)

                uci add_list dhcp.lan.dhcp_option="3,10.168.1.1" #config GW

                uci add_list dhcp.lan.dhcp_option="6,10.168.1.254,4.2.2.2" #config DNS

                uci commit dhcp

                reboot the Fon.
                SSH to 10.168.1.254. Login as root with the password you set.

The laptop will be acting as the default gateway. This way, all traffic can be easily captured going out to the Internet. For this set up to work correctly, the laptop must be configured to accept traffic from the Fon and forward it out an interface connected to the Internet.

    On Linux and other *nix based OS, iptables can be configured in Masquerade mode to allow traffic forwarding. I’ve created a bash script to easily allow users to configure their computes to do this. {DOWNLOAD}
    On Windows, Internet Connection Sharing (ICS) needs to be enabled on the interface connected to the Internet. The interface connected to the Fon should have an IP address of 10.168.1.1 netmask 255.255.255.0
    Everything should be set up and all packets should be flowing through your evil gateway.
