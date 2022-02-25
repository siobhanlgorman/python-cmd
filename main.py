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
    creates results_file1.html in root
    """
    cmd = "touch results_file1.html"
    returned_value = subprocess.call(cmd, shell=True)
    print("1")


create_results_file1()


def move_results_file1_into_branch1():
    """
    Copies results_file1 from root into branch1.
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
