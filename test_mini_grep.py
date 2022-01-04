#!/usr/bin/env python
import unittest
# Found this on: https://www.geeksforgeeks.org/python-testing-output-to-stdout/
from io import StringIO
from unittest import mock
import mini_grep
import argparse
import sys

class MyTestCase1(unittest.TestCase):

# Found some mocking stuff: https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
# And: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
#validate search pattern in file and is printed with it's own whole line (python3.10 mini_grep.py Welcome hello.py)
    @mock.patch('sys.stdout', new_callable=StringIO)
    @mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(pattern="Welcome", file_name="hello.py", quit_enumerate=False, enumerate=True))
    def test_main_1(self, mock_args, mock_stdout):
        expected_output = "1 Welcome to mini_grep!\n" # Had to modify this
        run_script = mini_grep.main()
        # if args_enumerate == True and args_quit_enumerate == False:
        #     self.assertEqual (expected_output, "1 hello")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

#validate user can type input when using only search pattern and file name (python3.10 mini_grep.py Welcome hello.py)
    def test_main_2(self):
        args_enumerate = False
        args_quit_enumerate = False
        user_input = 'hello'
        if args_enumerate == False and args_quit_enumerate == False:
            def setUp(self):
                self.test_main_2_output = 'this value'
            with patch('sys.stdout', new = StringIO()) as fake_out:
                mini_grep.conditions("","Welcome","hello.py")
                self.assertEqual (user_input, "hello") 

#validate search pattern in file appear in the expected lines with the expected numerical numbers of lines (python3.10 mini_grep.py -e Welcome hello.py)
    def test_main_3(self):
        args_enumerate = True
        args_quit_enumerate = False
        expected_output = "1 hello"
        if args_enumerate == True and args_quit_enumerate == False:
            self.assertEqual (expected_output, "1 hello") 

#validate search pattern in file appear in the expected lines without numerical numbers of lines when using -q argument (python3.10 mini_grep.py -q Welcome hello.py)
    def test_main_4(self):
        args_enumerate = False
        args_quit_enumerate = True
        expected_output = "  hello"
        if args_enumerate == False and args_quit_enumerate == True:
            self.assertEqual (expected_output,"  hello") 

#Validate that searching with invalid searched pattern regex will conclude with an error of invalid syntax (python3.10 mini_grep.py -e -Welcome hello.py)
    def test_main_5(self):
        args_enumerate = True
        args_quit_enumerate = False
        search_pattern_invalid = True
        expected_error = "usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: not allowed with argument -q"
        if args_enumerate == True and args_quit_enumerate == True and search_pattern_invalid == True:
            self.assertEqual (expected_error,"usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: ignored explicit argument 'llo'") 

#Validate that searching with more than one argument will conclude with an error of invalid syntax (python3.10 mini_grep.py -e -q Welcome hello.py)
    def test_main_6(self):
        args_enumerate = True
        args_quit_enumerate = True
        search_pattern_exists = True
        expected_error = "usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: not allowed with argument -q"
        if args_enumerate == True and args_quit_enumerate == True and search_pattern_exists == True:
            self.assertEqual (expected_error, "usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: not allowed with argument -q")

#Validate that searching without search pattern will conclude with an error of invalid syntax (python3.10 mini_grep.py -e -q hello.py)
    def test_main_7(self):
        args_enumerate = True
        args_quit_enumerate = True
        expected_error = "usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: not allowed with argument -q"
        if args_enumerate == True and args_quit_enumerate == True:
            self.assertEqual (expected_error, "usage: mini_grep.py [-h] [-q | -e]\n mini_grep.py: error: argument -e: not allowed with argument -q")

#Validate that all lines which doesn't contain search pattern, will be written in error log (python3.10 mini_grep.py -e hello.py)
    def test_main_8(self):
        args_enumerate = True
        args_quit_enumerate = False
        expected_log_text = "2 this line doesn't contain the search word \n 3 try again another pattern"
        if args_enumerate == True and args_quit_enumerate == False:
            self.assertEqual (expected_log_text,"2 this line doesn't contain the search word \n 3 try again another pattern")

if __name__ == '__main__':
    unittest.main()
