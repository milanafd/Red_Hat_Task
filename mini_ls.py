import argparse
import os
import logging
import argparse
import pwd
import datetime
import stat

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="myapp.log",
                    filemode="w",
                    format=Log_Format,
                    level=logging.ERROR)

logger = logging.getLogger()

#USEG:
#python3.10 mini_ls.py -r
#[Python v] [file     ][arg]

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', dest='recursive', action='store_true', help='Recursive')
    parser.add_argument('-file_name', dest='file_name', action='store_true', help='File name')
    # parser.add_argument('--path', help= 'Path') 
    args = parser.parse_args()
    # os.chdir(args.path)

    coditions(args, args.recursive, args.file_name)

def coditions(args, recursive, file_name):
    if file_name == False and recursive == False:
        print(find_file_information_when_no_args_exists(args))

    if file_name == False and recursive == True:
        print(find_file_list_recursivley(args))    
  
    
def find_file_information_when_no_args_exists(args):
    path='.'
    for entry in os.listdir(path):
        statinfo = os.stat(entry)
        epoch_time = os.path.getmtime(entry)
        datetime_time = datetime.datetime.fromtimestamp(epoch_time)
        print(f'{stat.filemode(statinfo.st_mode)} ', end="")
        print(f'{pwd.getpwuid(os.stat(entry).st_uid).pw_name} ', end="")
        print(f'{entry}')
        print(f'{datetime.datetime.fromtimestamp(epoch_time)} ', end="")


def find_file_list_recursivley(args):
    path='.'
    for entry in reversed(os.listdir(path)):
        print(entry)       
  

if __name__ == '__main__':
    main()
