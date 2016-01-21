##Automated DNS Zone Transfer Shell Script {:.blog-post-title}

February 8, 2012
{:.blog-post-meta}


![Alt text](../blog_img/PICTURE.jpg)

DNS zone transfers are not new and a general considered bad if misconfigured to allow transfers from anywhere.  Zone transfers will disclose all DNS entries and corresponding IP address for  a given DNS zone. This is great for all your other DNS server to keep records in sync, but not so good if you're trying to limit the visibility into your network by an attacker. There has been a lot of talk about this information gathering technique and a quick Google search will likely find better and fully detailed explanations.

I'd like to share a quick script I threw together today to test a zone transfers on a list of DNS servers.  It is a simple BASH script that calls dig. You supply it with a domain and file containing IP addresses of DNS server.

Usage: dns_zone_xfr.sh DOMAIN FILE

You'll need to remove the .txt extension and chmod +x dns_zone_xfr.sh to run.

Download: [dns_zone_xfr.sh](/static/uploads/dns_zone_xfr.sh.txt)