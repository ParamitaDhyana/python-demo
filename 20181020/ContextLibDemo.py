from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

class Query(object):

    def __init__(self,name):
        self.name=name

    # def __enter__(self):
    #     print('begin')
    #     return self
    
    # def __exit__(self,exc_type,exc_value,traceback):
    #     if exc_type:
    #         print('Error')
    #     else:
    #         print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')

# with create_query('Bob') as q:
#     q.query()


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield 
    print('<%s>' % name)

# with tag('h1'):
#     print('hello')
#     print('world')

# @contextmanager
# def closing(thing):
#     try:
#         yield thing
#     finally:
#         thing.close()

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)