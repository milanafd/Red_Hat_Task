import logging
import re
import argparse

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="myapp.log",
                    filemode="w",
                    format=Log_Format,
                    level=logging.ERROR)

logger = logging.getLogger()

#USEG:
#python3.10 mini_grep.py -e Welcome hello.py
#[Python v] [file     ][arg][pattern][searched file]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', type=str, metavar='', help="This is the search pattern")
    parser.add_argument('file_name', type=str, metavar='', help="File we are searching in")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', dest='quit_enumerate', action='store_true', help='Quit enumerate')
    group.add_argument('-e', dest='enumerate', action='store_true', help='Enumerate')
    args = parser.parse_args()
    
    conditions(args, args.pattern, args.file_name)


def conditions(args, pattern, file_searched):
    if args.enumerate == False and args.quit_enumerate == False:
        print(input()) 

    if args.enumerate == False and args.quit_enumerate == True:
        with open(file_searched, "r") as file:
            for line in (file):
                if re.search(pattern, line):
                    print(line)       
                else:
                    logger.error("Match wasn't found in line, enumeration is canceled.") 
 
    if args.enumerate == True and args.quit_enumerate == False:
        with open(file_searched, "r") as file:
            for number, line in enumerate(file):
                if re.search(pattern, line):
                    print(str(number + 1) + " " + line)       
                else:
                    logger.error("Match wasn't found in line " + str(number + 1)) 
   

if __name__ == '__main__':
    main()
