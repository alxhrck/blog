##Updating Splunk DHCP App MAC Address List {:.blog-post-title}

February 26, 2014
{:.blog-post-meta}


![Alt text](/static/img/splunk-mac-vendors.png)

UPDATE: I discovered that the IEEE OUI list is much more comprehensive. I've update the script to parse this file instead.

I've been using Splunk to monitor my DHCP server with Linux DHCP for some time now. It provides good insight into the devices connecting to my network and how often IP address are being requested. The one issue I noticed with the app was the short list of MAC OUI (Organizational Unique Identifier, the first 24-bits of a MAC address). The app uses a CSV file of MAC address and the assigned organization, but this file is not comprehensives and is missing many manufactures. This causes some inaccurate graphs when using the app.

I wrote a Python script to take the [IEEE manufacturer database](http://standards.ieee.org/develop/regauth/oui/oui.txt) and convert it to the correctly formatted CSV file for Linux DHCP. The script outputs dhcpd_mac-vendorname.csv which can be placed in **$SPLUNKHOME/etc/apps/dhcpd/lookups** for use by the Splunk app.

You can grab the Python script from GitHub <https://github.com/alxhrck/public/blob/master/ieee-oui-parse.py>.