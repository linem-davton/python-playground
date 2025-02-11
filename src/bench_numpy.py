import numpy as np
import math


def bench_multiply():
    """Benchmark function for numpy multiplication."""
    m1 = 1000
    rng = np.random.default_rng()
    a = rng.random((m1, m1))
    b = rng.random((m1, m1))
    c = a @ b
    print(c)


if __name__ == '__main__':
    bench_multiply()
    print(math.floor(13.2323532523 * 100)/100)
