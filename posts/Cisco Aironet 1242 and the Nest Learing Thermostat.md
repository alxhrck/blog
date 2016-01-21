##Cisco Aironet 1242 and the Nest Learing Thermostat {:.blog-post-title}

June 13, 2014
{:.blog-post-meta}

I've been having issues with the Nest reporting 'Offline' every hour or so within the app. The thermostat would comeback 'Online' if I deliberately moved in front of it or otherwise woke it up. I realized this issue must be related to the device sleeping to conserve power.  I use a Cisco Aironet 1242 WAP for my home wireless and decided to dig into it's configuration. After many failed debugging and configuration attempts, I think the issue has finally be solved by adding the following configuration item:

`beacon dtim-period 3`

I also set the speeds to 802.11g standards and the activity-timeout to 600.

`speed  basic-12.0 basic-18.0 basic-24.0 basic-36.0 basic-48.0 basic-54.0`

`dot11 activity-timeout unknown default 600`

`dot11 activity-timeout client default 600 maximum 600`

The DTIM-period is how often the a wireless client in power save mode should check a buffer for data. The Cisco default is 2, which tells the client check after every other beacon. Increasing this value to 3 seems to work the best with the Nest.

 

Resources:

<https://supportforums.cisco.com/discussion/11685611/nest-thermostats>

<http://www.cisco.com/c/en/us/td/docs/wireless/controller/7-4/configuration/guides/consolidated/b_cg74_CONSOLIDATED/b_cg74_CONSOLIDATED_chapter_01001110.html>

<https://www.juniper.net/techpubs/software/junos-security/junos-security10.0/junos-security-swconfig-wlan/wlan-ax411-access-point-dtim-period-understanding.html>