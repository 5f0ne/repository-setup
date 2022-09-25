import os
import shutil
import argparse

from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path of the directory in which the repository shall be created")
parser.add_argument("--name", "-n", type=str, required=True, help="Name of the new repository")
parser.add_argument("--type", "-t", choices=["module", "lib"], required=True, help="Create either a module or a lib")
args = parser.parse_args()

repositoryDir = os.path.join(args.path, args.name)

print("################################################################################")
print("")
print("Repository Setup by 5f0")
print("Creates the basic repository structure for python projects")
print("")
print("Current working directory: " + os.getcwd())
print("")
print("Target directory: " + args.path)
print("Name of new repository: " + args.name)
print("")
print("Creation Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print("")
print("################################################################################")
print("")

if(not os.path.isdir(repositoryDir)):
    shutil.copytree(args.type + "-files", repositoryDir)
    if(args.type == "module"):
        os.mkdir(os.path.join(repositoryDir, "example"))
    if(args.type == "lib"):
        os.mkdir(os.path.join(repositoryDir, "src"))
    print("Repository of type " + args.type + " created successfully under " + repositoryDir + "!")
else:
    print(repositoryDir + " already available!")

print("")
print("################################################################################")
print()