# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# USAGE
# python3 regex_search_021418_1.py

import re, os

#####################################
# USER INPUT
#####################################

# get user supplied folder or folder path
# TEST:  ../docs/testTxtFolder

folder_path_input = input("Please enter the folder or folder path of the text files you wish to search with a regex expression.\n")

# get user supplied regular expression
# TEST:  (doggy)

regex_input = input("Please enter the regex expression you want to search for:\n")

#####################################
# END USER INPUT
#####################################

#####################################
# FOLDER ANALYSIS, FIND TEXT FILES
#####################################

# # get current working directory as string value

# current_program_dir = os.getcwd() # aka. cwd

# # get the relative path from current working directory (where your program is) to the inputted folder
# # this allows you to generate a list of strings of the absolute path to the files
# # KEY POINT:  join this string to a filename to get it's actual path for purposes of using this program

# relPath_from_cwd_to_inputFolder = os.path.relpath(folder_path_input,current_program_dir)
# print(relPath_from_cwd_to_inputFolder) # for testing

# def relPath_from_cwd_to_inputFolder(folder_path_input,current_program_dir):
# 	# check if the inputted folder path is an absolute path or a relative path
# 	# if it's an absolute path
# 	# if it's a relative path
# 	pass


# get a list of all the `.txt` files in the folder

# code a way to search deeper into any additional folders for `.txt` files

# EXPECTED OUTPUT:
# ['docFolderL1', 'doc1.txt', 'doc3.txt', 'doc2.txt']

file_list_processing = os.listdir(folder_path_input) # return list of filename strings for each file in the `path` arg

# print(file_list_processing) # for testing

# # get the absolute path of the file names
# # path is relative to the main program
# # NOTE:  this means .. to leave current folder of main program
# # usng os.path.join() should allow this file path to work on any OS running this program

# def file_list_absPath_gen(file_list_processing):
# 	file_absPath = [] # empty list for absolute paths
# 	for filename in file_list_processing:
# 		new_path = os.path.join(folder_path_input,filename) # take the relative path to input folder and join it to the filename to create the full file path
# 		# print(new_path) # for testing
# 		file_absPath.append(new_path)
# 	return file_absPath

# file_list_absPath_final = file_list_absPath_gen(file_list_processing)
# print(file_list_absPath_final) # for testing

# # get the relative path of the file names

# def file_list_relPath_gen(file_list_processing):
# 	pass

# revise the list so the file list has strings of full paths to each of the files (whether relative or absolute)
# since the user supplied the path in either form, the resulting list will use that form
# no need to convert between absolute or relative paths

def file_list_fullPath_gen(file_list_processing):
	file_fullPath_item = [] # empty list for absolute paths
	for filename in file_list_processing:
		new_path = os.path.join(folder_path_input,filename) # take the relative path to input folder and join it to the filename to create the full file path
		# print(new_path) # for testing
		file_fullPath_item.append(new_path)
	return file_fullPath_item

file_list_fullPath_final = file_list_fullPath_gen(file_list_processing)
print("The file list with full paths for each folder or file is below.\n") # for testing
print(file_list_fullPath_final) # for testing


# check each item in file_list_processing to see if it's a folder
# if it is, go deeper into it and get text files
# this may be a function that recursively calls itself as you can have nested folders
# add each text file to list `file_list_final`

searchable_folder_list = [] # should be the string path of each folder

txt_file_list = [] # should be the string path of each text file

def folder_finder(folder_path_input):
	initial_folder = os.listdir(folder_path_input) # gets list of contents within the initially supplied folder
	# cycle through the contents and check if it is a folder
	# if it's a folder, add it to the `searchable_folder_list`
	pass

def file_finder(folder_path_input):
	# the code takes a folder_path_input and gets list of contents
	# cycle through each item in the returned list
	# check if it's a file
	# for this program it's specifically a `.txt` ending file
	# for modifying this program for other document types you may alter this in the future
	pass

def add_txt_to_file_list_final(text_file):
	pass

# cycle through folder list (file_list_processing) to find sub-directories

# cycle through {{searchable_folder_list}} to find files
# as you cycle through file list
# if file is a .txt add it to list {{txt_file_list}}

#####################################
# END FOLDER ANALYSIS, FIND TEXT FILES
#####################################

# print results to the terminal screen

