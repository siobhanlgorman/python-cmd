# import module
import os
import subprocess
from datetime import datetime
import calendar
import time
from pathlib import Path


def create_branch1():
    """
    Creates branch1 folder in root
    """
    cmd = "mkdir branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("0")


create_branch1()


def create_results_file1():
    """
    creates results_file1.html in branch1 dir
    """
    cmd = "touch results_file1.html"
    returned_value = subprocess.call(cmd, shell=True)
    print("1")


create_results_file1()


def move_results_file1_into_branch1():
    """
    Copies results_file1 from test_results dir into test_results_backup dir.
    """
    cmd = "mv results_file1.html branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("2")


move_results_file1_into_branch1()


def move_branch1_into_test_results():
    """
    Moves branch1 into test_results dir.
    """
    cmd = "cp -r branch1 test_results"
    returned_value = subprocess.call(cmd, shell=True)
    print("3")


move_branch1_into_test_results()


def move_branch1_results_folder_into_backup_dir():
    """
    Copies branch1 from test_results dir into test_results_backup dir.
    """
    cmd = "cp -r test_results/branch1 test_results_backup"
    returned_value = subprocess.call(cmd, shell=True)
    print("4")


move_branch1_results_folder_into_backup_dir()


def rename_backup_folder_with_datestamp():
    """
    Renames branch1 in backup dir with datestamp attached.
    """

    os.rename(
        "test_results_backup/branch1",
        time.strftime("test_results_backup/branch1_%Y-%m-%d_%I-%M-%S_%p"),
    )
    print("5")


rename_backup_folder_with_datestamp()


def delete_original_branch1_in_test_results():
    """
    Deletes original branch1 from test_results directory.
    """
    cmd = "rm -r test_results/branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("6")


delete_original_branch1_in_test_results()


def delete_original_folder_created_in_root():
    """
    Deletes original branch1 from root.
    """
    cmd = "rm -r branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("7")


delete_original_folder_created_in_root()


# def move_dir_into_backup():  # copy sub_dir or create empty and move? append timestamp
#     """
#     copies test_results dir into test_results_backup dir
#     """
#     cmd = "cp -r test_results/branch1 test_results_back_up/tests_batch2_back_up"
#     returned_value = subprocess.call(cmd, shell=True)

#     print("C")


# move_dir_into_backup()

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
