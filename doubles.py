import random
import re
import string

import numpy as np
import python_rust
from pytest_benchmark.fixture import BenchmarkFixture


# Python traditional ZIP version
def count_doubles(val: str):
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


def count_once(val: str):
    total = 0
    c1 = val[0]
    for c2 in val[1:]:
        if c1 == c2:
            total += 1
        c1 = c2
    return total


def count_doubles_regex(val: str):
    double_re = re.compile(r"(?=(.)\1)")
    return len(double_re.findall(val))


def count_double_numpy(val: str):
    ng = np.fromstring(val, dtype=np.byte)
    return np.sum(ng[:-1] == ng[1:])


# Benchmark it
# generate random letters to test it
x = 8_000_000
val = "".join(random.choice(string.ascii_letters) for _ in range(x))
# val = 'A' * x
# val = 'AB' * (x//2)


def test_python_zip(benchmark: BenchmarkFixture):
    benchmark(count_doubles, val)


def test_python_regex(benchmark: BenchmarkFixture):
    benchmark(count_doubles_regex, val)


def test_python_once(benchmark: BenchmarkFixture):
    benchmark(count_once, val)


def test_python_numpy(benchmark: BenchmarkFixture):
    benchmark(count_double_numpy, val)


def test_rust_zip(benchmark: BenchmarkFixture):
    benchmark(python_rust.count_doubles_zip, val)


def test_rust_once(benchmark: BenchmarkFixture):
    benchmark(python_rust.count_doubles_once, val)


def test_rust_bytes(benchmark: BenchmarkFixture):
    benchmark(python_rust.count_doubles_bytes, val)


def test_rust_bytes_unsafe(benchmark: BenchmarkFixture):
    benchmark(python_rust.count_doubles_unsafe, val)