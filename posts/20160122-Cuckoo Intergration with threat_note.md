##Cuckoo Intergration with threat_note {:.blog-post-title}

January 22, 2016
{:.blog-post-meta}


[threat_note](https://github.com/defpoint/threat_note) is a great, light-weight webapp that gives security researchers, incident responders and other security practitioners a place to collect indicators of compromise. threat_note has been designed to integrate with a variety of 3rd party services, allowing users to quickly pull in data to provide more context around an indicator. 

One useful integration is with [Cuckoo Sandbox](https://www.cuckoosandbox.org). Cuckoo is a malware analysis sandbox used to detonate and examine suspicious executables. Cuckoo collects execution data including how a system is modifed, any dropped files and network communication.  Enabling Cuckoo integration in threat_note is simple and quickly allow the investigator to grab IOCs from a previously analyzed sample. 

Start by login to the system running Cuckoo and running the API server.

`  python ./cuckoo/utils/api.py -H 0.0.0.0 `

Next, in threat_note enable Cuckoo Sandbox in the *Settings > File*. Then configure the fields for *Cuckoo Host* and *Cuckoo API Port*. 

![Alt text](/static/img/enable-cuckoo.png)

![Alt text](/static/img/config-cuckoo.png)

The *Import from Cuckoo* button will appear on the *Dashboard*, clicking it will take you to the import page.

![Alt text](/static/img/import-cuckoo.png)

Select the analysis task you would like to import and optionally, add a campaign or list of tags.

All file hashes, domains and IP address detected by Cuckoo will now be available in the threat_note interface.

![Alt text](/static/img/from-cuckoo.png)

This simple yet powerful integration enables you to quickly import a large set of indicators from a tool that generates high quality IOCs.