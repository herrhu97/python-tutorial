
from urllib.request import urlopen
from contextlib import closing

try:
    f = open('/Users/herrhu/Desktop/python-tutorial/builtin-module/a.txt', 'r')
    data = f.read()
    print(data)
finally:
    if f:
        f.close()

with open('/Users/herrhu/Desktop/python-tutorial/builtin-module/a.txt', 'r') as f:
    data = f.read()
    print(data)


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

from contextlib import contextmanager

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with Query('Bob') as q:
    q.query()

with create_query('Bob') as q:
    q.query()


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
