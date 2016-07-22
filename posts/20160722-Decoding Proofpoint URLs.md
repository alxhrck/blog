##Decoding Proofpoint URLs {:.blog-post-title}

July 22, 2016
{:.blog-post-meta}

![eek_haxxor](/static/img/phishing2.png)

Recently, I started reviewing messages found in the corporate spam box, setup for people to alert us on any phishy messages getting past the spam filters, in an attempt to automatically analyze new phishing links. 


Fortunately, or unfortunately (depending on where you sit), Proofpoint offers a service to a block links to malicious and suspicious sites. This service rewrites the suspect URL in each email with a link that redirects through the Proofpoint URL Defense system.  A parameter of this new URL is the encoded version of the suspect link.


The challenge was to decode the URL parameter from Proofpoint and return it to its original format. This is for two purposes, first and formost, this allows me to not get blocked by URL Defense and second, it prevents sewed results. 


Another interesting aspect of URL Defense is in the real-time alerts. These alerts contain information around who clicked the suspect link, from where and which link. Proofpoint is tricky how they include the suspect URL. They insert zero width space (Unicode: \u200b) between each character, basically invalidating the link. You know, for safety.


Thankfully, [Warren Raquel](<https://github.com/warquel>) had already written some code to decode the suspect link parameter of the rewritten URL, I simply scriptified his code, and added removal of those funky zero width spaces. 




Modified ppdecode <https://github.com/alxhrck/other_scripts/blob/master/ppdecode.py>


Original ppdecode <https://github.com/warquel/ppdecode>

