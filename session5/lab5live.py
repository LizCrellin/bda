
import time
'''def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)
'''
'''
import multiprocessing as mp
if __name__ == '_main__':
    start = time.time()
    p1 = mp.Process(target=foo)
    p2 = mp.Process(target=foo)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''

# or better approach
# (good structure to follow)

import multiprocessing as mp

def foo(sec):
    print("Sleeping", sec)

# ---SERIAL CODE---
def serial_runner():
    start = time.time()
    foo(3)
    end = time.time()
    print(end-start)
# ---PARALLEL CODE---
def parallel_runner():

    p1 = mp.Process(target=foo, args=[1])
    p2 = mp.Process(target=foo, args=[2]) 
    p3 = mp.Process(target=foo, args=[3])

    start=time.time()


    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end=time.perf_counter()
    print(f'Parallel: {end-start} second(s)')


if __name__ == '__main__':
    # run here!
    serial_runner()
    parallel_runner()




