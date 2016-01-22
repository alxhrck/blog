##Bind Query Logging to Splunk from pfSense {:.blog-post-title}

May 21, 2014
{:.blog-post-meta}


I wanted to add a secondary DNS server (NS2) to my home network as a backup to the primary DNS server (NS1) to provide redundancy in case there is a connectivity issue with the primary (NS1). I went ahead and installed the Bind package on my pfSense gateway via web GUI and configured it as a Slave server. You need to configure a 'View' on the Bind server for zone transfers or look-ups to work.
view

![Alt text](/static/img/bind-view.png)
*View settings. A simple, get-it-to-work setup*

After configuring a View and a new Zone, zone transfers from my primary DNS server started to work along with queries. At this point, and after a minor tweak to the DHCP server, I had accomplished what I needed.

Then I thought I'd take it a step further. I'm already logging queries from NS1 to Splunk, so why not log NS2 queries as well? This way I can monitor when NS2 is being used and which devices are making queries. Logging on pfSense is done simply with syslogd and is not very configurable via the web GUI. I needed to get creative with how I setup Bind logging since pfSense is already sending firewall events to Splunk over standard UDP 514 (That is another blog post in itself).

There are two major issues I needed to overcome to make this work. First, I needed to get syslogd working inside the Bind (named) jail that pfSense creates. This was as simple as adding '-l /cf/named/var/run/log' to the syslogd_flag in /etc/defaults/rc.conf.  On FreeBSD, '-l' specifies where syslogd should put additional log sockets, required when using syslogd within a chroot jail.

`syslogd_flags="-s -l /cf/named/var/run/log" # Flags to syslogd (if enabled).`

Second, Bind needed to be configured to log via syslog but because the pfSense web GUI is responsible for generating the named.conf, editing this file via the command line is not recommend.  The Bind settings screen allows for additional custom Options to be inserted into the options section of the configuration file. By adding a "};" before the logging stanza, you essentially close the Options stanza and insert Logging or any other configuration. The web GUI will add the closing "};" which is why it's omitted from the screenshot below.

![Alt text](/static/img/customOptions.png)

To complete the setup, added an entry to syslog.conf to pass all local6 log entries to the Splunk server.

![Alt text](/static/img/syslogconf.png)

