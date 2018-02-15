# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

import re, os

# get user supplied folder or folder path

folder_path_input = input("Please enter the folder or folder path of the text files you wish to search with a regex expression.\n")

# get user supplied regular expression

regex_input = input("Please enter the regex expression you want to search for:\n")

# get a list of all the `.txt` files in the folder

file_list = os.listdir(folder_path_input) # return list of filename strings for each file in the `path` arg

# TODO:  code a way to search deeper into any additional folders for `.txt` files
# print results to the terminal screen

