# Using the 'match' statement: this is similar to switch
def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 403:
            return "Unauthorized"
        case 404:
            return "Not found"
        case _:
            "Something is not right"


print(http_error(400))


def nothing_func():
    """
    Functions that do not return anything will still return 'None'
    """
    pass


print(nothing_func())


def show_thy_arguments(*args):
    for arg in args:
        print(arg)


show_thy_arguments(1, 2, 3, 4, "foo", "bar")


def show_thy_kwargs(**kwargs):
    for kw in kwargs:
        print(f"{kw}: f{kwargs[kw]}")


show_thy_kwargs(foo="bar", moo="cow")


def square():
    return lambda x: x * x


print(square()(2))
