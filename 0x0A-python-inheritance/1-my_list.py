#!/usr/bin/python3
class MyList(list):
    """
    A class to customize the list class
    """
    def print_sorted(self):
        """
        prints a list in ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
