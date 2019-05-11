# using decorators to factor-out administrative logic
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# better:
@cache # new one is lrucache
def weblookup(url):
    return urllib.urlopen(url).read()

# caching decorator -  your utils libraries should be full of these
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc
