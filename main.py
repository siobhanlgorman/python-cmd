# import module
import os
import subprocess
import time


def main():
    create_branch1()
    create_results_file1()
    move_results_file1_into_branch1()
    move_branch1_into_test_results()
    move_branch1_results_folder_into_backup_dir()
    rename_backup_folder_with_datestamp()
    delete_original_branch1_in_test_results()
    delete_original_folder_created_in_root()
    print("Cycle complete")


def create_branch1():
    """
    Creates branch1 folder in root
    """
    cmd = "mkdir branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("0 created branch1")


def create_results_file1():
    """
    creates results_file1.html in root
    """
    cmd = "touch results_file1.html"
    returned_value = subprocess.call(cmd, shell=True)
    print("1 created results_file1.html")


def move_results_file1_into_branch1():
    """
    Copies results_file1 from root into branch1.
    """
    cmd = "mv results_file1.html branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("2 copied results_file1.html into branch1")


def move_branch1_into_test_results():
    """
    Moves branch1 into test_results dir.
    """
    cmd = "cp -r branch1 test_results"
    returned_value = subprocess.call(cmd, shell=True)
    print("3 copied branch1 dir into test results dir")


def move_branch1_results_folder_into_backup_dir():
    """
    Copies branch1 from test_results dir into test_results_backup dir.
    """
    cmd = "cp -r test_results/branch1 test_results_backup"
    returned_value = subprocess.call(cmd, shell=True)
    print("4 copied branch1 into test_results_backup dir")


def rename_backup_folder_with_datestamp():
    """
    Renames branch1 in backup dir with datestamp attached.
    """

    os.rename(
        "test_results_backup/branch1",
        time.strftime("test_results_backup/branch1_%Y-%m-%d_%I-%M-%S_%p"),
    )
    print("5 added datestamp to backup copy of branch1")


def delete_original_branch1_in_test_results():
    """
    Deletes original branch1 from test_results directory.
    """
    cmd = "rm -r test_results/branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("6 deleted branch1 from test_results dir")


def delete_original_folder_created_in_root():
    """
    Deletes original branch1 from root.
    """
    cmd = "rm -r branch1"
    returned_value = subprocess.call(cmd, shell=True)
    print("7 deleted branch1 in root dir")


if __name__ == "__main__":
    main()
