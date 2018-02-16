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
# REGEX
#####################################

textRegex_1 = re.compile(r'(\.txt)') # https://regexr.com/3ksc4

#####################################
# END REGEX
#####################################


#####################################
# FOLDER ANALYSIS, FIND TEXT FILES
#####################################

# get a list of all the `.txt` files in the folder

# code a way to search deeper into any additional folders for `.txt` files

# EXPECTED OUTPUT:
# ['docFolderL1', 'doc1.txt', 'doc3.txt', 'doc2.txt']

file_list_processing = os.listdir(folder_path_input) # return list of filename strings for each file in the `path` arg



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
# print("The file list with full paths for each folder or file is below.\n") # for testing
# print(file_list_fullPath_final) # for testing


# check each item in `file_list_fullPath_final` to see if it's a folder

searchable_folder_list = [] # should be the string path of each folder


txt_file_list = [] # should be the string path of each text file

# NOTE:  the inputted folder list should already in the form of string paths from `file_list_fullPath_gen` for each filename that was discovered using `os.listdir()`
def analyze_file_folders(file_path_list):	
	for item in file_path_list:
		# want this condition first to skip other steps
		# if item in searchable_folder_list:
		# 	pass # if the file path item is already in the `searchable_folder_list` then skip it
		# check if the file is a folder
		if os.path.isdir(item):
			# if it is a folder store the folder (folder path) in `searchable_folder_list`
			# then run this function on the item again to append additional folders to `searchable_folder_list`
			# eventually it should run out of folders
			
			searchable_folder_list.append(item)

		elif os.path.isfile(item):
			# else if the item is a file store it in `searchable_file_list` so that we can later sort out the `.txt` files out of everything else

			analyze_file_for_textFile(item)
		else:
			print("It seems you've run into an error.")
			break # break the loop here


def analyze_file_for_textFile(item_file_path):
	# a function that analyzes whether said file is a text file and then store it in `txt_file_list`
	
	# if the regex pattern for .txt endings is found in the file item's string file path
	if textRegex_1.search(item_file_path):
		# add the item/item path to txt_file_list
		txt_file_list.append(item_file_path)
	else:
		pass # otherwise skip it and keep moving



# cycle through the folder list and sub folders to find all text files
# this should result in a list of all `.txt` files (i.e. file paths)
# use list `file_list_fullPath_final`

analyze_file_folders(file_list_fullPath_final)

# it should also result in a list of all folders that need to be searched again for nested or deeper sub-folders

# print("Folders found in `searchable_folder_list` are:\n")
# print(searchable_folder_list) # for testing

# if more folders are appended as the loop progresses, it only stops when no more folders have been appended to `searchable_folder_list`
for folder in searchable_folder_list:
	# get the listing of files within the folder
	# folder should be a folder path
	get_files_within_folder = os.listdir(folder) # the result of this is a list of file names not paths
	# add the folder path to file names to get file path
	# requires a loop
	# `folder` should be the base path to join to a filename
	# `item` will be a filename that needs to be joined to a folder path
	full_path_list = []
	for item in get_files_within_folder:
		file_path_fullItem = os.path.join(folder,item)
		full_path_list.append(file_path_fullItem)

	# this function requires a list of file and/or folder paths to work remember?
	# `full_path_list` should now be a list of full path strings that lead to the files you want to analyze
	analyze_file_folders(full_path_list)

# EXPECT:  
# ['../docs/testTxtFolder/doc1.txt', '../docs/testTxtFolder/doc3.txt', '../docs/testTxtFolder/doc2.txt', '../docs/testTxtFolder/docFolderL1/doc4.txt', '../docs/testTxtFolder/docFolderL1/docFolderL2/doc5.txt']

print("Folders found in `txt_file_list` are:\n") # for testing
print(txt_file_list) # for testing


#####################################
# END FOLDER ANALYSIS, FIND TEXT FILES
#####################################

#####################################
# TEXT DATA EXTRACTION
#####################################

# open each file in the `txt_file_list` for reading
# find the user supplied regex expression target
# copy a certain segment or number of characters around that expression target (maybe using regex substitution to grab more)
# print the result to the terminal screen
# close each of the files as you finish the analysis



#####################################
# END TEXT DATA EXTRACTION
#####################################





