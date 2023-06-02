from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup function
PROJECT_NAME="Adult Census Income Prediction"
VERSION="0.0.2"
AUTHOR="Pritam Chaudhari"
DESCRIPTION="This Project for Ineuron Internship End To End"
REQUIREMENTS_FILE_NAME="requirements.txt"

HYPHEN_E_DOT="-e ."

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention is reqirements.txt file

    return this fuction is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
            
        return requirement_list
 
setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
inatall_requires=get_requirements_list()

)