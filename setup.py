from setuptools import setup, find_packages
import os
from pathlib import Path
from typing import List
def read_requirements(file_path: str) -> List[str]:
    line_list:list = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                line = line.strip()
                if line and line != '-e .':
                    line_list.append(line)
        
                    
    except FileNotFoundError:
        print("requirements.txt file not found.")
        return []
    return line_list
setup(
    name='network_security',
    version='0.1.0',
    author='Abhiraj Singh Solanki',
    author_email='abhirajsolanki2005@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    description='A package for network security tools and utilities.',
    long_description='This package provides various tools and utilities for enhancing network security.',
    long_description_content_type='text/markdown')