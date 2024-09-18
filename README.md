# Getting Started

```BASH
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Benchmarks

```BASH
perf stat -r 10 python3 benchmarks.py # -r 10 means 10 repetitions of the benchmark

 Performance counter stats for 'python3 bench_numpy.py' (10 runs):

            470.31 msec task-clock                       #    0.999 CPUs utilized               ( +-  0.60% )
                 2      context-switches                 #    4.252 /sec                        ( +- 27.69% )
                 0      cpu-migrations                   #    0.000 /sec
             7,363      page-faults                      #   15.656 K/sec                       ( +-  0.01% )
     2,072,670,582      cycles                           #    4.407 GHz                         ( +-  0.05% )
     8,513,490,133      instructions                     #    4.11  insn per cycle              ( +-  0.00% )
     1,098,498,613      branches                         #    2.336 G/sec                       ( +-  0.00% )
         3,825,255      branch-misses                    #    0.35% of all branches             ( +-  0.09% )
                        TopdownL1                 #      4.7 %  tma_backend_bound
                                                  #      4.5 %  tma_bad_speculation
                                                  #     18.6 %  tma_frontend_bound
                                                  #     72.2 %  tma_retiring             ( +-  0.05% )

           0.47072 +- 0.00281 seconds time elapsed  ( +-  0.60% )
```
