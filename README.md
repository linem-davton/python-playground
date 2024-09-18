# Getting Started

```BASH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Benchmarks

```BASH
perf stat -r 10 python3 benchmarks.py # -r 10 means 10 repetitions of the benchmark
```
