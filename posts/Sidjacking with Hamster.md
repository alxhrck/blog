##Sidejacking with Hamster {:.blog-post-title}

November, 12 2009
{:.blog-post-meta}

Websites need to somehow protect users’ passwords when sent from the browser to the server.  To do this, sites will encrypt the password into a session cookie and pass that securely to the server.  An issue arises because the website server does not or cannot preform a check as to the authenticity from where this session cookie coming from.  Sidejacking or session hijacking is when an attacker captures network traffic, specifically web traffic containing the users authentication token (session cookie) for a website, and then replays the token to gain access to the user's account.

A set of tools released by Errata Security (http://erratasec.blogspot.com)  called Ferret/Hamster automate this process and provide a web interface to replay the cookies. Ferret is a specially built packet sniffer that collects only packets containing session cookie.  The session ID and associated website are entered into a file.  Hamster is a web proxy that runs locally and reads from the file that Ferret created for easily replaying of the captured cookies.

Ferret/Hamster 2.0 can be downloaded from <http://hamster.erratasec.com/>.  The tool comes as either a Windows binary or *nix source that can easily be complied.  I have had some issues with Hamster crashing on Windows 7, but Ferret was able to run just fine.

After obtain the executables by either downloading or compiling them, run ferret -W from the command line to list available network adapters.
ferret -W

The output on my test machine of ferret -W. I'm interested in interface 1 (eth0), 3 (wlan0) and 4 (bnep0 - my 3G cellphone modem).

To start sniffing for session cookies traveling from your machine to the Internet, run ferret -i interface.  On Windows you will be using the number associated with the interface. On Linux you are able to specific eth0, wlan0, etc.  Session cookies will be collected and stored in a file called hamster.txt in the directory with the executables.

In a command prompt, navigate to where ferret/hamster is saved a start hamster.  You will notice that the proxy will be running on http://127.0.0.1:1234.  To access this web page, you must set your browser to use a web proxy running on port 1234.  I like to use a Firefox plug-in called FoxyProxy to easily change the browsers proxy settings.


Now that ferret is collecting sessions and hamster is ready to replay those sessions, use a browser to navigate to http://hamster. You should see a list of IP addresses that sessions have been collected from. When you click on one of the targets, a list of websites will appear on the left hand panel.  Click on one and with any luck, hamster should automatically pass the session cookie and redirect you to the post authenticated webpage.


**Defense**

You see how easy it is for an attacker to obtain access to your websites.  There are several preventative measures users can take to protect themselves. Do not connect unsecure wireless access points. Connecting to unsecured wireless access points will make you the most vulnerable because you do not know and cannot trust other computers connected in the area.  That being said, much of the time it is impractical to totally avoid using a wireless connection so use a VPN connection or SSH tunnel to encrypt network traffic sent from your machine.  I have found that sites using SSL such as gmail (not by default) are less likely to be prone to this attack.  Be aware of what high impact sites you are visiting.  Most of the time attackers are not interested low impact sites Facebook or Twitter profiles, but rather, they are looking to gain access to high impact sites like corporate web email and financial websites. The simplest action any web user can do to mitigate the risk of sidejacking is to logout of the website because once you logout, the authentication session cookie is no longer valid.  Morel of the story, always be weary when you are connected to untrusted wired or wireless networks.

"Just because you are paranoid, it doesn’t mean they are not out to get you"
