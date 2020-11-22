def create_key():
    kname = input("Enter KeyPair name : ")
    qname = input("Enter name by which you want to query : ")
    savename = input("Enter the pem file name you want to save the key.")
    subprocess.run("aws ec2 create-key-pair — key-name {} — query “{}” > {}.pem".format(
        kname, qname, savename), shell=True)


def create_securityGroup():
    des = input("Description for security group : ")
    gname = input("Enter security group name : ")
    subprocess.run(
        "aws ec2 create-security-group — description “{}” — group-name “{}”".format(des, gname), shell=True)

    print("\nNow configuring the security group, by default it allows all ip.")
    subprocess.run(
        "aws ec2 authorize-security-group-ingress — group-name {} — protocol tcp — port 22 — cidr 0.0.0.0/0".format(gname))
    print("\n Security Group is Successfully Created and Configured. ")


def provisionEC2():
    security_id = input("Enter Security Group ID : ")
    count = int(input("How many OS you want to provision : "))
    keyname = input("Enter Key Name : ")
    print("Instance Type will be t2.micro by default ...")
    print("By default Image AMI will be LinuxAMI ...")
    x = input("Do you want to enter Image ID and Instance type manually? (y/n) : ")
    if x == "y":
        instance_type = input("Enter Instance Type : ")
        Image_ID = input("Enter Image ID : ")
    else:
        instance_type = "t2.micro"
        Image_ID = "ami-052c08d70def0ac62"

    subprocess.run("aws ec2 run-instances — image-id {} — count {} — instance-type {} — key-name {} — security-group-ids {}".format(
        Image_ID, count, instance_type, keyname, security_id), shell=True)


def createEBS():
    print("By Default Volume Type will be gp2, size of 1GB and Availability Zone, Mumbai, ap-south-1b")
    i = input("Do you want to enter EBS Block configuration manually? (y/n) : ")
    if i == "y":
        v_type = input("Enter Volume Type : ")
        size = int(input("Enter size (in GB) : "))
        zone = input("Enter Availability Zone : ")
    else:
        v_type = "gp2"
        size = 1
        zone = "ap-south-1b"

    subprocess.run(
        "aws ec2 create-volume — volume-type {} — size {} — availability-zone {}".format(v_type, size, zone), shell=True)
    print("\n EBS Block Volume Successfully Created ...")


def attachEBS():
    print("Enter EBS Volume ID : ")
    print("Enter Instance ID : ")
    subprocess.run(
        "aws ec2 attach-volume — volume-id {} — instance-id {} — device /dev/sdf".format(v_id, instance_id))
    print("\n EBS Volume attached successfully ...")
