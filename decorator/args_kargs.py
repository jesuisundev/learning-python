def test_args_kwargs(*args, **kwargs):
    for arg in args:
        print("another arg through *argv:", arg)

    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

test_args_kwargs('toto', 'tata', super="toto")