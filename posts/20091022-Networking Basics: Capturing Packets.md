##Networking Basics: Capturing Packets {:.blog-post-title}

October 22, 2009
{:.blog-post-meta}

I recently gave a presentation (slides - pdf) about packet sniffing to a group of students interested in the security field. It was an interesting experience given the fact that it was the second time I have presented something in two years, and desperately need public speaking practice. Overall I feel it went well and look forward to giving another presentation in the future.

This is a recap of the presentation with some additional comments. Understanding how to capture packets is one of the core competencies a network administrator should have. Packet captures can help you understand how packets are constructed, troubleshoot connectivity issues, and monitor traffic from known or unknown applications. Tools like Wireshark and TCPDump make watching data fly across the network so easy to do and are invaluable when trouble shooting or preforming reconnaissance on a network. Let's break it down from the beginning.

Network communication (lolz interwebz) is based around, depending on who you ask, a five (Internet) or seven (OSI) layer model. I like to cover the five layer model because it is a bit simpler and contains the most interesting stuff. These layers encapsulate the data in a standard frame that all network devices, from a network interface card (NIC), to a switch or router, can read and process.

These Matryoshka dolls represent the OSI layers.The smallest is the application layer (Layer 5). The largest is the physical layer (Layer 1)

When you capture a packet you are capturing this data and because this is an open model, anyone can easily figure out how to decapsulate the frame. Wireshark (www.wireshark.org), in particular, is a great tool for viewing how data is arranged on a network. This tool is freely available and has great filtering abilities. TCPDump (www.tcpdump.org) is similar to Wireshark, but in a lightweight, command line form.

Normally, computers will only process packets that are labeled with their MAC (layer 2) and IP (layer 3) address. This won't cause any problems with capturing packets going to and from your own machine, like when you are browsing the web, but it would cause problems if you want to see what  other computer is doing on the network. The default for most packet sniffing tools is to put the a wired NIC in promiscuous mode though exactly how this is done is OS specific. Promiscuous mode allows the packet capturing tool to receive every packet, regardless of MAC or IP.  If you are on a switched network (which is more than likely) you will still only see packets destined for your machine because switches are smart enough to know what port a MAC address is attached to and will only send packets to the right port.  To see all traffic in this situation you need a network tap or Cisco SPAN port enabled.  Hubs on the other hand are dumb, and will send packets out all ports with no regards as to what MAC it is destined for.

Capturing all packets that are traveling across the wireless LAN are just as easy to catch. I won't say that operating systems based on Unix are the only ones that can do this, but the are by far the only ones that can do this easily. Do some research into AirPCAP and related wireless cards if you are looking at using Windows for this. The wireless equivalent to promiscuous mode is monitor mode. Mointor modes will let your wireless card see every packet that is sent on surrounding radio waves. This mode must be supported by the WLAN card drivers. Aircrack-ng wiki has a good chart of Linux compatible cards that support monitor mode. Most tools do not automatically put wireless cards into this mode, but #iwconfig wlan0 mode monitor is a simple command that will allow that card to hear all and see all.

That about wraps it up the very basics of capturing network traffic on both wired and wireless connections. I will be posting more information about other tools you can use alongside live and offline packet captures, but until then, check out these extremely helpful sites:

PacketLife.org cheatsheets - <http://packetlife.net/library/cheat-sheets/>

TheInterW3bs.com packet capture cheatsheet - <http://theinterw3bs.com/docs/PacketSniffCraft-CheatSheet.pdf>

Basic Wireshark filters - <http://openmaniak.com/wireshark_filters.php>

Wireshark tutorial - <http://www.security-freak.net/tools/wireshark/wireshark.html>