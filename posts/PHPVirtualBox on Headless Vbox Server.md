##PHPVirtualBox on Headless Vbox Server {:.blog-post-title}

May 11, 2011
{:.blog-post-meta}


![Alt text](/static/img/vbox.png)

Update: This was an older post which was recreated after server rebuild. All steps haven't fully been tested with the latest environment but you should find the information you need to get you going in the right direction.

I prefer to run VirtualBox on a headless (no GUI) Linux server which allow more hardware resources to be dedicated to virtual machines instead of the pretty window manager. Setting up phpvirutalbox to manage a headless VirtualBox 4.2 server is a simple process that will allow you to easily manage and administer virtual machines from a web browser.

My environment: CentOS 5.5 x64, VirtualBox 4.2, php 5.2.10 and httpd 2.2.8 (apache2)

1) Download and install ViritualBox for Linux Hosts
http://www.virtualbox.org/wiki/Linux_Downloads
note: you could also install/configure the VBox repositories for Debain or RHEL based   system

2) Download and install VirtualBox 4.0.4 Oracle VM VirtualBox Extension Pack which is needed for USB support and console access.

`# VBoxManage extpack install FILE`

3) Configure VirtualBox environment

4) Install apache and php using your distros package manager 
`# yum install httpd php`

5) Download phpViritualBox
wget http://code.google.com/p/phpvirtualbox/downloads/detail?name=phpvirtualbox-4.0-4b.zip&can=2&q=

6) Extract the the zip file and copy to the webserver’s root directory
`# unzip phpvirtualbox-4-2.zip`
`# cp –r phpvirtualbox-4-2 /var/www/html/phpvirtualbox`

7) Set the correct permissions to the phpvirtualbox directory so apache can read from the web directory
`# chown apache:apache -R /var/www/html/phpvirtualbox`

8) Edit phpvirtualbox/config.php
Add your vbox user, password, location, and disable authentication (for now)

	var $username = 'vbox';
	var $password = 'vboxpass';
	var $location = 'http://127.0.0.1:18083/phpvirtualbox'
	var $noAuth = true;

9) Run the following command with the IP of your server
`# su vbox -c "/usr/bin/vboxwebsrv -b -H 127.0.0.1 --logfile /dev/null >/dev/null`

Be sure Apache has been started (service httpd start).

10) Add the command above with your server IP to /etc/rc.local
This will allow Viritualbox and it's web interface to run at startup.

11) Navigate to http://SERVER-IP/phpvirtualbox