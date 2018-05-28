from multiprocessing import Pool
from timeit import timeit
from test1 import Solution, sample
import time


def testfun(ntimes):
     res = timeit("Solution().maxAverage2(sample, 1012)",
                  setup="from __main__ import Solution, sample", number=ntimes)
     return res
if __name__ == "__main__":
    for i in range(1, 16):
        print i, 'started, -------'
        a = time.time()
        testcases = [30 for _ in range(33)]
        testcases.append(10)
        pool = Pool(i)
        results = pool.map(testfun, testcases)
        pool.close()
        pool.join()
        print sum(results)
        print time.time() - a
        print i, 'finished, -------'