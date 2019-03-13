# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:27:55 2019

@author: admin
"""
import os
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape

directory=r"C:\Users\admin\Documents\Python Scripts"
os.chdir(directory)
template_directory=r"C:\Users\admin\Documents\Python Scripts\dashboard"
final_directory=r"C:\Users\admin\Documents\Python Scripts\dashboard\resources"

statuses = {"System 1": "Down", "System 2": "Up", "System 3": "Up", "System 4": "Down"}

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
os.chdir(template_directory)
template = env.get_template('index_template.html')

output = template.render(statuses=statuses) 
print(output)
os.chdir(final_directory)


Html_file= open("index.html","w")
Html_file.write(output)
Html_file.close()


