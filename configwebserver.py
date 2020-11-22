def configure_webserver():
	print("Installing Apache Webserver Software ...\n")
	subprocess.run("yum install httpd -y",shell=True)
	print("Starting WebServer Service ...")
	subprocess.run("systemctl start httpd",shell=True)
	print("Disabling firewall temporary ...")
	
	print("Now put your files in /var/www/html folder and restart the service ...")