'''import time
import threading

def foo():
    print("In foo...")
    print("Running...")
    time.sleep(1)

# Serial runner
def serial_runner():
    start = time.perf_counter()
    for i in range(3):
        foo()
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')

# Parallel thread runner
def parallel_runner1():
    start = time.perf_counter()

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t3 = threading.Thread(target=foo)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time.perf_counter()
    print(f'Parallel: {end - start} second(s)')

if __name__ == '__main__':
    print("Serial", serial_runner())
    print("Parallel", parallel_runner1())'''




import time, threading

def boo(secs):
    print("In boo...")
    print("Running...")
    time.sleep(secs)

# Serial runner
def serial_runner():
    start = time.perf_counter()
    boo(1)
    boo(2)
    end = time.perf_counter()
    return end - start

# Parallel thread runner
import concurrent.futures
def parallel_runner_f(secs):  # secs is a list [1,2,3,4,,,]
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:#
        executor.map(boo,secs)

    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    print("Serial", serial_runner())
    print("Parallel", parallel_runner_f([1,2]))


