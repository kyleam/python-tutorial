"""Running a program versus importing it

To test, open up Terminal and cmd.exe:

  $ python strjoin.py 'aa' 'bb'

Now open up ipython and import strjoin.py:

  >>> import strjoin
  >>> strjoin.join_strings('aa', 'bb')

Notice that, when importing, the code under `if __name__ == '__main__'`
is not excecuted. 
"""
import sys


def join_strings(string1, string2):
    """Join two strings"""
    joined = string1 + string2
    return joined

if __name__ == '__main__':
    string1, string2 = sys.argv[1], sys.argv[2]
    result = join_strings(string1, string2)
    print('joining {} and {}: {}'.format(string1, string2, result))
