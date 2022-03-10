import os
import subprocess
import time


def dirCleanup():
    move_branch1_results_folder_into_backup_dir()  # step 1
    rename_backup_folder_with_datestamp()  # step 2
    print("Cycle complete")


def move_branch1_results_folder_into_backup_dir():
    """
    Moves dir 1 from test_results dir into test_results_backup dir.
    """
    # cmd = "move C:Users/VDC/Desktop/test_results/1 test_results_backup" (this is Shane's path)
    cmd = "move C:/Users/siobh/Desktop/My_Projects/python-cmd/test_results/1 test_results_backup"
    returned_value = subprocess.call(cmd, shell=True)
    print("1 moved dir 1 into test_results_backup dir")


def rename_backup_folder_with_datestamp():
    """
    Renames dir 1 in backup dir with datestamp attached.
    """
    old_folder_name = os.path.join("test_results_backup", "1")
    new_folder_name = os.path.join(
        "test_results_backup", time.strftime("1_%Y-%m-%d_%I-%M-%S_%p")
    )
    os.rename(old_folder_name, new_folder_name)
    print("2 added datestamp to backup copy of dir 1")


dirCleanup()
