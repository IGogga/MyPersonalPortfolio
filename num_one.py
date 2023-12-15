import functools


def cache(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for k in args:
            print(k)
            print(args)
            # Для словаря
            if type(k) == type(dict()):
                args = dict(k)
                ndict = {}
                for i in k:
                    newlist = []
                    nlist = [];
                    nlist.append(i), nlist.append(k[i])
                    for j in nlist:
                        cache_key = (j,) + tuple(kwargs.items())
                        if cache_key not in cache:
                            cache[cache_key] = func(j, **kwargs)
                        newlist.append(cache[cache_key])
                    ndict[newlist[0]] = newlist[1]
                    if len(ndict) == len(k):
                        return ndict

            # Для списка
            elif type(k) == type(list()):
                nlist = []
                for i in list(k):
                    cache_key = (i,) + tuple(kwargs.items())
                    if cache_key not in cache:
                        cache[cache_key] = func(i, **kwargs)
                    nlist.append(cache[cache_key])
                    if len(nlist) == len(list(k)):
                        return nlist

            # Для кортежа
            elif type(k) == type(tuple()):
                nlist = []
                for i in list(k):
                    cache_key = (i,) + tuple(kwargs.items())
                    if cache_key not in cache:
                        cache[cache_key] = func(i, **kwargs)
                    nlist.append(cache[cache_key])
                    if len(nlist) == len(list(k)):
                        return tuple(nlist)

            # Для простых значений
            else:
                cache_key = (k,) + tuple(kwargs.items())

            if cache_key not in cache:
                cache[cache_key] = func(k, **kwargs)
            return cache[cache_key]

    return wrapper


@cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


# print(fib())
# print(fib(20))
# print(fib(50))
# print(fib(35))
# print(fib(10))
# print(fib(100))

# print("list: ", fib([1, 10], [1, 100]))  # [1, 55]
# print("tuple: ", fib((100, 99))) # (354224848179261915075, 218922995834555169026)
# print("dictionaty: ", fib({10: 7}, {10: 8}, {10: 9}))  # {55:13}
