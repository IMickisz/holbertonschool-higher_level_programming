#!/usr/bin/python3
"""
1-my_list.py
Test file: 1-my_list.txt
Class: MyList
Method(s): print_sorted
To test this method, run:
python3 -m doctest ./test/1-my_list.txt
"""


class MyList(list):
    """
    A class to customize the list class (inherite from list)
    """
    def print_sorted(self):
        """
        prints a list in ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
