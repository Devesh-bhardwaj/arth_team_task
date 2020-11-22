import socket
# FETCHING IP ADDRESS --> THIS ASSUMES YOU HAVE ACTIVE INTERNET CONNECTION
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def configure_namenode_hdfssite_file(path_of_folder):
    print("Moving to your Hadoop Configuration Directory ...")
    os.chdir("/etc/hadoop")

    mytree = ET.parse('hdfs-site.xml')

    myroot = mytree.getroot()

    property_ = SubElement(myroot, 'property')
    name = SubElement(property_, 'name')
    name.text = 'dfs.data.dir'

    value = SubElement(property_, 'value')
    value.text = path_of_folder

    print("Printing the configured hdfs-site.xml file ...")
    print(prettify(myroot))

    mytree.write("hdfs-site.xml")


def configure_namenode_coresite_file(ip):
    print("Moving to your Hadoop Configuration Directory ...")
    os.chdir("/etc/hadoop")

    mytree = ET.parse('core-site.xml')

    myroot = mytree.getroot()

    property_ = SubElement(myroot, 'property')
    name = SubElement(property_, 'name')
    name.text = 'fs.default.name'

    value = SubElement(property_, 'value')
    print("The port number by default is 9001")
    value.text = 'hdfs://{}:9001'.format(ip)

    print("Printing the configured core-site.xml file ...")
    print(prettify(myroot))

    mytree.write("core-site.xml")


def configure_datanode_hdfssite_file():
    print("Moving to your Hadoop Configuration Directory ...")
    os.chdir("/etc/hadoop")

    mytree = ET.parse('hdfs-site.xml')

    myroot = mytree.getroot()

    property_ = SubElement(myroot, 'property')
    name = SubElement(property_, 'name')
    name.text = 'dfs.data.dir'

    value = SubElement(property_, 'value')
    value.text = path_of_folder

    print("Printing the configured hdfs-site.xml file ...")
    print(prettify(myroot))

    mytree.write("hdfs-site.xml")
