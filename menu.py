os.system("clear")
print("				---------------     WELCOME TO THE WORLD OF INTEGRATION     ---------------")
print()
print("					Please choose any of the below technology you want to implement.\n")
print()
print("****************************************************************************************************************************************\n")

print("Press the respective keyboard keys to implement it.\n")

print("1. Implement a Hadoop Cluster\n")
print("2. Achieve some common functionalities of RHEL8 Linux.\n")
print("3. Check some of the ML Algos with basic concepts of DSA\n")
print("4. Achieve some of the functionality of AWS with single click assumed you have AWSCLI on your base system and configured for access.\n")
print("5. Setup and run a docker container on RHEL8 as Base system.\n\n")

opt = int(input("Enter your choice : "))
mf=""
if opt==1:
	os.system("clear")
	print("			***************         SETTING UP HADOOP CLUSTER         ***************\n")
	print("Now, setting up MASTER NODE.\n")
	i= input("Do you have a Folder where the storage has to be mounted?(y/n)")
	if i=="y":
		mf = input("Enter your folder directory: ")
	else:
		mf = input("Creating a folder for you in root directory, please enter name of your folder : ")
		os.system("mkdir /{}".format(mf))
		print("Folder is created...")

	print("Now, we are updating your hdfs-site.xml file to setup NameNode ...\n")
	
	configure_namenode_hdfssite_file(mf)

	print("We are adding this system as Master Node by default ...\n")
	print("Fetching IP address, please wait ...")	
	print("Now, we are configuring core-site.xml file to setup NameNode ...\n")
	
	configure_namenode_coresite_file(ip)
	
	print("Now that everything is configured, we have to first format the Folder to create a new INode Table for the cluster ...")
	print("Formatting ....")
	os.system("mkfs.ext4 {}".format(mf))
	print("Formatted using ext4 type ...")

	print("NOW, STARTING  NAMENNODE SERVICE ...\n")
	os.system("hadoop-daemon.sh start namenode")
	
	c = input("Do you want to check status of your NameNode running or not?(y/n)")
	if c=="y":
		os.system("jps")
		quit()
	else:
		quit()
	
	print("*******************************************************************************************************")
	print()
	print("Now setting up Data Node ...\n")
	print("Remotely Connecting to the DataNode for configuration ...\n")
	ip_data = input("Enter IP Address of DataNode : ")
	print("Configuring DataNode Remotely, this may take some time ...\n")

elif opt==4:
	os.system("clear")
	print("			 ****************    ACHIEVE AWS FUNCTIONALITIES WITH SINGLE CLICK    ****************")
	print()
	print("Choose below options : ")
	
	print("a. Create Key-Value Pair")
	print("b. Create and Configure Security Group")
	print("c. Provision EC2 instance")
	print("d. Create EBS Volume")
	print("e. Attach EBS Volume to EC2 instance for usage.")

	q = input("Enter your choice : ")
	if q=="a":
		create_key()
	elif q=="b":
		create_securityGroup()
	elif q=="c":
		provisionEC2()
	elif q=="d":
		createEBS()
	elif q=="e":
		attachEBS()
		

	
elif opt==5:
	os.system("clear")
	print("		   *******************        STARTING THE DOCKER SERVICE ON THE BASE SYSTEM        *******************\n")
	start_docker_service()
	print("Docker service started on the base system...\n")
	print("Please choose below options for docker functionalities ...\n")
	
	print("a. Pulling Image")
	print("b. Launching Container")
	print("c. Remove Image")
	print("d. Remove Container")	
	print("e. Check Logs")
	print("f. Copy files from Base system to Continer")
	print("g. Copy files from Container to Base system")
	print("h. Check running containers")
	print("i. Attach to the existing container")
	print("j. To start the initially created container")
	print("k. Stop the running container")

	di = input("Enter your choice : ")

	if di=="a":
		pull_image()
	elif di=="b":
		launch_container()
	elif di=="c":
		remove_image()
	elif di=="d":
		remove_container()
	elif di=="e":
		see_logs()
	elif di=="f":
		cp_base_to_cont()
	elif di=="g":
		cp_cont_to_base()
	elif di=="h":
		see_the_running_cont()
	elif di=="i":
		get_terminal()
	elif di=="j":
		start_exist_cont()
	elif di=="k":
		stop_running_docker()

else:
	print("Sorry, this function is in developing process ...")
	quit()

	



