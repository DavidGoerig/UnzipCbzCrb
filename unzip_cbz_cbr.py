#!/usr/bin/env python

__author__ = "David Goerig"
__version__ = "1.0.1"
__maintainer__ = "David Goerig"
__email__ = "davidgoerig68@gmail.com"
__status__ = "Production"

import sys
import getopt
from pathlib import Path
import pathlib
import sys
import yaml

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def usage():
    print(bcolors.HEADER + "Welcome to the tools.\n" + bcolors.ENDC)
    print(bcolors.UNDERLINE + "Usage:" + bcolors.ENDC)
    print(bcolors.BOLD + "\t-h or --help:" + bcolors.ENDC + " print usage.")
    print(bcolors.BOLD + "\t-p or --path:" + bcolors.ENDC + " set the path of the directory. Otherwise it will take the directory set in the settings.yaml.")
    print(bcolors.BOLD + "\t-d or --dirname:" + bcolors.ENDC + " name of the directory after unzipping.")
    print(bcolors.BOLD + "\t-e or --extension:" + bcolors.ENDC + "name of the extension (cbr or cbz).")

def loop_in_directory(path, dirname, extension):
    pathlist = Path(path).rglob('*.' + extension)
    for pathes in pathlist:
        # because path is object not string
        path_in_str = str(pathes)
        print(path_in_str)

def load_yaml_settings(file):
    with open(file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            sys.exit()

def print_launch_settings(path, dirname, extension):
    print(bcolors.HEADER + "Launch settings:\n" + bcolors.ENDC)
    print(bcolors.OKGREEN + "\tPath:\t\t\t" + bcolors.ENDC + path)
    print(bcolors.OKGREEN + "\tName of the directory:\t" + bcolors.ENDC + dirname)
    print(bcolors.OKGREEN + "\tExtension:\t\t" + bcolors.ENDC + extension)


def main(argv):
    yaml_file = load_yaml_settings("settings.yaml")
    path = yaml_file["settings"]["path"]
    dirname = yaml_file["settings"]["dir_name"]
    extension = yaml_file["settings"]["extension"]
    try:
        opts, args = getopt.getopt(argv, "hp:d:e:", ["help", "path=", "dirname=", "extension="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-d", "--dirname"):
            dirname = arg
        elif opt in ("-e", "--extension"):
            extension = arg
    print_launch_settings(path, dirname, extension)
    loop_in_directory(path, dirname, extension)

if __name__ == "__main__":
    main(sys.argv[1:])