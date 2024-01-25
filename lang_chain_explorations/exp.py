# LAMBDAS

""" foo = lambda x: x + 1

print(foo(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'a-five')]
pairs.sort(key=lambda pair: pair[1])
pairs

print(pairs) """

# CLASSES

class MyClass:
    """Add a private field with getters and setters"""
    def __init__(self):
        self._my_field = 0

    @property
    def my_field(self):
        return self._my_field

    @my_field.setter
    def my_field(self, value):
        self._my_field = value
        
# write a new class that exposes methods to the user
class MyClass:
    def __init__(self):
        self._my_field = 0

    def get_my_field(self):
        return self._my_field

    def set_my_field(self, value):
        self._my_field = value