from lib.projects.performance.benchmark import Benchmark

class Component:
    def __init__(self, name: str = None):
        self._name = name

        # benchmark
        self._perf_analysis: bool = False
        self._benchmarker: Benchmark = Benchmark(self._name)
    
    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name