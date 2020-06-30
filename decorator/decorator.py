def escape_unicode(f):
    def wrap(*args, **kwargs):
        print(*args)
        print(**kwargs)
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city(test = 1):
    return 'Troms£'


northern_city()