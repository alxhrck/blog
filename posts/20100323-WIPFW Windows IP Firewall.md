##WIPFW Windows IP Firewall {:.blog-post-title}

March 23, 2010
{:.blog-post-meta}


For those looking for a full featured, scriptable and light weight firewall for Windows XP and Sever 2003 (or earlier) check out WinIPFW (http://wipfw.sourceforge.net). While versions on Windows prior to Vista have a built in firewall, it is limiting. The Windows firewall will not filter egress traffic and has poor logging capabilities. Fine grain filtering control of IP address, protocol and port of both ingress and egress traffic are all features of WinIPFW. Advanced logging of any desired traffic is possible as is the ability to create Windows batch script files for automatic configuration.

If you install WinIPFW blocking all in-bound and out-bound traffic you must specifically open ports for web browsing, etc. Also, always install and configure firewalls using a local console to avoid blocking remote administration services (SSH,VNC,RDP).
