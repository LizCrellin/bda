import multiprocessing as mp, time
def boo(sec):
    print("In boo...")
    time.sleep(sec)

# ---SERIAL CODE---
def serial_runner(secs):
    start = time.perf_counter()
    for sec in secs:
        boo(sec)
    end = time.perf_counter()
    print(end-start)

# ---PARALLEL CODE---
def parallel_runner(secs):
    processes = []
    start = time.perf_counter()
    for sec in secs:
        p = mp.Process(target = boo, args=[sec])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    end = time.perf_counter()
    print(f"Parallel: {end-start} second(s)")


if __name__ == '__main__':
    # run here!
    secs = [1,2,3,4,5]
    serial_runner(secs)
    parallel_runner(secs)

