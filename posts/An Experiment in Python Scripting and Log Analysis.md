##An Experiment in Python Scripting and Log Analysis {:.blog-post-title}

June 15, 2011
{:.blog-post-meta}


![Alt text](/static/img/world.png)

I’ve created this simple Python script, in an attempt to dive in and learn a little about the language while creating a useful tool to help with log analysis. This script preforms WHOIS queries on IP address found in a log file, then extract the registered country found in the returned information.  Lip2cc.py (Logged IP to Country Code), as I call it, is an extremely simple start to what I have envisioned.

Currently all IP address are required to be pulled out of a log file (say access or secure log) with some bash fu and stored in a separate text file.  Eventually I will work this function into the script so all that is required is the systems log file. Below is a simple bash script to find all IP addresses attempting to log into the system.

`# cat secure*| cut -d" " -f11 | egrep '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' |egrep -v "\<Bye\>" | egrep -v [a-z2\!]$ |sort -u > ips.txt`

Bonus list all usernames attempting logins:

`# cat /var/log/secure* | cut -d" " -f8,9 | egrep '\<^user\>'|sed s/user/user:/ |sort -u`

I’m sure this is not the first IP to country code look-up tool, and it is definitely not the first Python script which quires WHOIS data, but it was an excellent Python learning experience.

Lip2cc.py takes one command line argument, -f (–file). This is required and should be a newline-delimitated file of IP address. I open the file and read in every line into a Python list, which allows me to easily loop through and lookup every IP given. I start by querying whois.iana.org looking for which regional registry the selected IP resides in.  From there I am able to extract the correct URL needed to perform a WHOIS lookup. A second WHOIS query is done against the regional registry. I locate and extract the country field then print it to the screen.

The online Python documentation, Beginning Python by Magnus Lie Hetland and inspiration from some previously created whois.py scripts were valuable resources. This was a great to be able to explore many interesting aspects of Python functions, network sockets, text parsing, arg passing and regular expression searching.  All in all, not to bad for my first jump into Python.

Download [lip2cc.py](https://github.com/alxhrck/public/blob/master/lip2cc.py)