# using decorators to factor-out administrative logic
# biz logic is opening a url and looking up web page
# admin logic to factor out is caching the lookup
# mixes logics and is not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


# BETTER:
@cache  # this is lrucache, only for pure functions (not random.random, etc.)
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
