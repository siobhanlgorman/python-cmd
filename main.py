# import module
import os
import subprocess

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


def create_dir():
    """
    Creates a directory called experiment in the root directory.
    """
    cmd = "mkdir experiment"
    returned_value = subprocess.call(cmd, shell=True)
    print("1")


create_dir()


def create_file_and_populate():
    """
    Creates a file called hello.txt in root directory and populates it
    with print("Hello World") command. Closes file after populating.
    No use of subprocess module here.
    """
    cmd = open("hello.txt", "w")
    cmd.write('print("Hello World")')
    cmd.close()
    print("2")


create_file_and_populate()


def move_file_into_dir():
    """
    Moves file hello.txt into experiment directory.
    """
    cmd = "mv hello.txt experiment"
    returned_value = subprocess.call(cmd, shell=True)
    print("3")


move_file_into_dir()


def run_file():
    """
    Executes content of hello.txt file.
    """
    cmd = "python3 experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
    print("4")


run_file()


def create_back_up_dir():
    """
    creates backup directory
    copies file into backup directory and renames
    """
    cmd = "mkdir experiment_back_up"
    returned_value = subprocess.call(cmd, shell=True)
    print("B")


create_back_up_dir()


def create_back_up_file():
    """
    copies file into backup directory and renames
    """
    cmd = "cp experiment/hello.txt experiment_back_up"
    returned_value = subprocess.call(cmd, shell=True)
    print("C")


create_back_up_file()


def delete_file():
    """
    Deletes hello.txt from experiment directory.
    """
    cmd = "rm experiment/hello.txt"
    returned_value = subprocess.call(cmd, shell=True)
    print("5")


delete_file()
