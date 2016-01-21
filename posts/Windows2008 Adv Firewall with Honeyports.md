##Windows 2008 Advanced Firewall with Honeyports {:.blog-post-title}

March 22, 2011
{:.blog-post-meta}

Windows 2008 has a fantastically good firewall, as long as you configure it properly. A honeyport is a listening port with no operational service that will log specific information about a connection that is made to it.  The idea is that only a port scanner will find this port and an attacker will further investigate. As defenders, we can use firewalls and honey ports in combination, as demonstrated by John Strand's (@strandjs) tech segment on Pauldotcom.com Security Weekly episode 203, to block potential attacks.


I've made very slight modifications to Strand's original script, including a "log" output to better track when port scans happen. I've also included a minimal Windows 2008 server firewall policy with web, file sharing and active directory ports open.  It has been packaged up with nc for windows and a few scripts to make things easy to run.  A couple caveats, you will need to modify some of the IP address within the rules to match your system. This can be done by navigating to the *rule* properties and selecting the *Scope* tab. Next you will need to change the default rule to block all incoming and outgoing.  Navigate to the properties *Windows Firewall with Advanced Security*.  In the *State* section you will see *Inbound connections* and *Outbound connections*. Both should be set to *Block*. Lastly, this could be used to create a denial of service condition where the attacker spoofs a legitimate IP, this is for learning purposes only and should not be used on production systems.


Now you may extract the contents of Win2k8-Honeyport.zip to C: and run *import_fw.cmd* to configure the new firewall rules. Launch *run_honeyport.cmd* to start monitoring for port scans and blocking potentially malicious connections. Scan you system with nmap (nmap -sS -sV -v -PN -A <IP_ADDR>)


A Windows 2003 version using wipfw is in the works. Download the [Win2k8-Honeyport.zip](http://alex.hrck.net/wp-content/uploads/2011/03/Win2k8-Honeyport.zip).


Ref: (http://pauldotcom.com/wiki/index.php/Episode203#Tech_Segment:__Windows_HoneyPorts)

Ref: (http://www.securityfocus.com/tools/139)
