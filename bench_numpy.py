import numpy as np


def bench_multiply():
    """Benchmark function for numpy multiplication."""
    rng = np.random.default_rng()
    a = rng.random((1000, 1000))
    b = rng.random((1000, 1000))
    print(np.multiply(a, b))


if __name__ == '__main__':
    bench_multiply()
