import os
import subprocess
import time


def main():
    create_branch_1()  # testing only
    create_results_file1()  # testing only
    move_results_file1_into_branch_1()  # testing only
    move_branch1_into_test_results()  # testing only
    move_branch1_results_folder_into_backup_dir()  # step 1
    rename_backup_folder_with_datestamp()  # step 2
    print("Cycle complete")


def create_branch_1():
    """
    Creates dir 1 folder in root for testing purpose only
    """
    cmd = "mkdir 1"
    returned_value = subprocess.call(cmd, shell=True)
    print("0 created dir 1")


def create_results_file1():
    """
    Creates results_file1.html in root for testing purpose only
    """
    cmd = "echo some text > results_file1.html"
    returned_value = subprocess.call(cmd, shell=True)
    print("1 created results_file1.html")


def move_results_file1_into_branch_1():
    """
    Moves results_file1 from root intodir 1 for testing purpose only
    """
    cmd = "move results_file1.html 1"
    returned_value = subprocess.call(cmd, shell=True)
    print("2 moved results_file1.html into dir 1")


def move_branch1_into_test_results():
    """
    Movesdir 1 into test_results dir for testing purpose only
    """
    cmd = "move 1 test_results"
    returned_value = subprocess.call(cmd, shell=True)
    print("3 moved dir 1 into test results dir")


def move_branch1_results_folder_into_backup_dir():
    """
    Moves dir 1 from test_results dir into test_results_backup dir.
    """
    cmd = "move C:/Users/siobh/Desktop/My_Projects/python-cmd/test_results/1 test_results_backup"
    returned_value = subprocess.call(cmd, shell=True)
    print("4 moved dir 1 into test_results_backup dir")


def rename_backup_folder_with_datestamp():
    """
    Renames dir 1 in backup dir with datestamp attached.
    """
    old_folder_name = os.path.join("test_results_backup", "1")
    new_folder_name = os.path.join(
        "test_results_backup", time.strftime("1_%Y-%m-%d_%I-%M-%S_%p")
    )
    os.rename(old_folder_name, new_folder_name)
    print("5 added datestamp to backup copy of dir 1")


if __name__ == "__main__":
    main()
