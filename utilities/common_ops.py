import json
import time
import xml.etree.ElementTree as ET


def get_time_stamp():
    return time.time()

####################################################################################################################
# Function Name:get_data
# Function Description: This function is used to get data from data.xml file
# Function Parameters: node_name
# Function Return: String - node value
####################################################################################################################
def get_data(node_name):
    # jenkins
    #root = ET.parse("../configuration/data.xml").getroot()
    # pytest
    root = ET.parse("./configuration/data.xml").getroot()
    return root.find('.//' + node_name).text

####################################################################################################################
# Function Name: read_json_file
# Function Description: This function is used to read json file
# Function Parameters: file_path
# Function Return: json file
####################################################################################################################
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
