import timeit
from timeit import Timer

# demonstrates time to create lists using different approaches


def create_with_concat():
    l = []
    for i in range(1000):
        l = l + [i]

def create_with_append():
    l = []
    for i in range (1000):
        l.append(i)

def create_with_comprehension():
    l = [i for i in range(1000)]

def create_with_constructor():
    l = list(range(1000))

t1 = Timer("create_with_concat()", "from __main__ import create_with_concat")
print("concat ", t1.timeit(number = 1000), "milliseconds")

t2 = Timer("create_with_append()", "from __main__ import create_with_append")
print("append ", t2.timeit(number = 1000), "milliseconds")

t3 = Timer("create_with_comprehension()", "from __main__ import create_with_comprehension")
print("comprehension", t3.timeit(number = 1000), "milliseconds")

t4 = Timer("create_with_constructor()",  "from __main__ import create_with_constructor")
print("constructor", t4.timeit(number = 1000), "milliseconds")

