import re
import string
import random
import python_rust
import numpy as np

# Python traditional ZIP version
def count_doubles(val):
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


def count_once(val):
    total = 0
    c1 = val[0]
    for c2 in val[1:]:
        if c1 == c2:
            total += 1
        c1 = c2
    return total

# Python REGEXP version
double_re = re.compile(r'(?=(.)\1)')

def count_doubles_regex(val):
    return len(double_re.findall(val))



def count_double_numpy(val):
    ng=np.fromstring(val,dtype=np.byte)
    return np.sum(ng[:-1]==ng[1:])


# Benchmark it
# generate 1M of random letters to test it
val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_python_zip(benchmark):
    benchmark(count_doubles, val)

def test_python_regex(benchmark):
    benchmark(count_doubles_regex, val)

def test_python_once(benchmark):
    benchmark(count_once, val)

def test_python_numpy(benchmark):
    benchmark(count_double_numpy, val)

def test_rust_zip(benchmark):
    benchmark(python_rust.count_doubles_zip, val)

def test_rust_once(benchmark):
    benchmark(python_rust.count_doubles_once, val)

def test_rust_bytes(benchmark):
    benchmark(python_rust.count_doubles_bytes, val)