# import module
import os
import subprocess
from datetime import datetime
import calendar
import time
from pathlib import Path

# assign directory
# directory1 = "mynewfolder"
# directory2 = "mynewfolder2"
# ext = ".html"

# cmd = "git --version"

# returned_value = subprocess.call(cmd, shell=True)


# def printhelloworld():
#     cmd1 = "mkdir mynewfolder mybackupfolder"
#     subprocess.call(cmd1, shell=True)
#     cmd2 = "touch hello.txt"
#     subprocess.call(cmd2, shell=True)
#     cmd3 = "mv hello.txt mynewfolder"
#     subprocess.call(cmd3, shell=True)
#     cmd4 = "cp mynewfolder/hello.txt mybackupfolder/hellobackup.txt"
#     subprocess.call(cmd4, shell=True)
#     cmd5 = "rm mynewfolder/hello.txt"
#     subprocess.call(cmd5, shell=True)


# printhelloworld()


# def move_dir_into_backup():  # copy sub_dir or create empty and move? append timestamp
#     """
#     copies test_results dir into test_results_backup dir
#     """
#     cmd = "cp -r test_results/tests_batch2 test_results_back_up/tests_batch2_back_up"
#     returned_value = subprocess.call(cmd, shell=True)

#     print("C")


# move_dir_into_backup()

import time
import os


# def change_name_to_time():
#     # Getting the path of the file
#     f_path = "C:/Users/siobh/Desktop/My_Projects/python-cmd/test_results_back_up/test_results_backup_batch/"

#     # Obtaining the creation time (in seconds)
#     # of the file/folder (datatype=int)
#     t = os.path.getctime(f_path)

#     # Converting the time to an epoch string
#     # (the output timestamp string would
#     # be recognizable by strptime() without
#     # format quantifers)
#     t_str = time.ctime(t)

#     # Converting the string to a time object
#     t_obj = time.strptime(t_str)

#     # Transforming the time object to a timestamp
#     # of ISO 8601 format
#     form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)

#     # Since colon is an invalid character for a
#     # Windows file name Replacing colon with a
#     # similar looking symbol found in unicode
#     # Modified Letter Colon " " (U+A789)
#     form_t = form_t.replace(":", "꞉")

#     # Renaming the filename to its timestamp
#     new_name = os.rename(f_path + "/" + form_t)
#     print(new_name)


def change_name_to_time():

    os.rename(
        "test_results_back_up/trbb",
        time.strftime("test_results_back_up/trbb_%Y-%m-%d_%I-%M-%S_%p"),
    )


change_name_to_time()

# def append_date():
#     folder_name = "C:/Users/siobh/Desktop/My_Projects/python-cmd/test_results_back_up/tests_batch2_back_up/"

#     datestring = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     cmd = "mv(folder_name, os.path.join(folder_name, datestring))"
#     returned_value = subprocess.call(cmd, shell=True)


# append_date()


# def rename_file():
#     """
#     Renames file and places in new dir
#     """
#     created_time = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
#     print(created_time)
#     filename = "test_results_back_up/tests_batch2_back_up"

#     new_filename = filename + "_" + created_time
#     print(new_filename)

# if not os.path.exists(new_filename):
# os.mkdir(new_filename)


# new_file_name = os.rename(
#     "test_results/tests_batch4",
#     "test_results_back_up/tests_batch4_back_up",
# )


# rename_file()

# def move_file_into_dir():
#     """
#     Moves file hello.txt into experiment directory.
#     """
#     cmd = "mv hello.txt experiment"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("3")


# move_file_into_dir()

# def rename_mulitple_files():
#     """
#     Renames all files in directory or all new directories
#     """
#     for file in os.listdir("/home/career_karma"):
# 	os.rename(file, f"/home/career_karma/old_{file}")

# a = "{}".format(datetime.datetime.now().strftime("%H:%M:%S"))
# def append_timestamp(filename):

#     timestamp = calendar.timegm(time.gmtime())
#     human_readable = datetime.datetime.fromtimestamp(timestamp).isoformat()
#     filename = test_results_back_up / tests_batch1
#     filename_with_timestamp = filename + "_" + str(human_readable)
#     return filename_with_timestamp


# print(append_timestamp("FILENAME"))

# def add_time_stamp_to_backup_dir():
#     renamed_folder = "test_results_back_up/tests_batch1".format(
#         datetime.datetime.now().strftime("%H:%M:%S")
#     )
#     return renamed_folder


# add_time_stamp_to_backup_dir()


# def create_dir():
#     """
#     Creates a directory called experiment in the root directory.
#     """
#     cmd = "mkdir experiment"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("1")


# create_dir()


# def create_file_and_populate():
#     """
#     Creates a file called hello.txt in root directory and populates it
#     with print("Hello World") command. Closes file after populating.
#     No use of subprocess module here.
#     """
#     cmd = open("hello.txt", "w")
#     cmd.write('print("Hello World")')
#     cmd.close()
#     print("2")


# create_file_and_populate()


# def move_file_into_dir():
#     """
#     Moves file hello.txt into experiment directory.
#     """
#     cmd = "mv hello.txt experiment"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("3")


# move_file_into_dir()


# def run_file():
#     """
#     Executes content of hello.txt file.
#     """
#     cmd = "python3 experiment/hello.txt"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("4")


# run_file()


# def create_back_up_dir():
#     """
#     creates backup directory
#     copies file into backup directory and renames
#     """
#     cmd = "mkdir experiment_back_up"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("B")


# create_back_up_dir()


# def create_back_up_file():
#     """
#     copies file into backup directory
#     """
#     cmd = "cp experiment/hello.txt experiment_back_up"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("C")


# create_back_up_file()


# def delete_file():
#     """
#     Deletes hello.txt from experiment directory.
#     """
#     cmd = "rm experiment/hello.txt"
#     returned_value = subprocess.call(cmd, shell=True)
#     print("5")


# delete_file()
