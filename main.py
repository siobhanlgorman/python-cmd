# import module
import os

# asssign directory
directory1 = "mynewfolder"
directory2 = "mynewfolder2"

# create a dir
def createdir():
    os.system("mkdir mydir")


def runthroughtestfiles():
    for filename in os.listdir(directory1):
        if filename.is_file():
            # f = os.path.join(directory, filename)
            # # checking if it is a file
            # if os.path.isfile(f):
            print(filename)


# def addfiletodir():
#     createdir()
#     os.system()
