# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# python3 regex_search_021418_1.py

import re, os

# get user supplied folder or folder path
# TEST:  ../docs/testTxtFolder

folder_path_input = input("Please enter the folder or folder path of the text files you wish to search with a regex expression.\n")

# get user supplied regular expression
# TEST:  (doggy)

regex_input = input("Please enter the regex expression you want to search for:\n")

# get a list of all the `.txt` files in the folder
# EXPECTED OUTPUT:
# ['docFolderL1', 'doc1.txt', 'doc3.txt', 'doc2.txt']

file_list = os.listdir(folder_path_input) # return list of filename strings for each file in the `path` arg



print(file_list)

# TODO:  code a way to search deeper into any additional folders for `.txt` files
# print results to the terminal screen

