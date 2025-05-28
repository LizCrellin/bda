import time
import concurrent.futures


def boo(sec):
    print("In boo...")
    print(f"Running for {sec} second(s)")
    time.sleep(sec)

# serial runner
def serial_runner(secs):
    start=time.perf_counter()
    for i in secs:
        boo(i)
    end=time.perf_counter()
    print(f'Serial: {end-start} second(s)')

# parallel running - futures
def parallel_runner(secs):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(boo, secs)
    end = time.perf_counter()
    print(f"Parallel runner{end-start}")


if __name__ == '__main__':
    #run here
    secs = [1,2,3,4,5,6]
    serial_runner(secs)
    parallel_runner(secs)



'''
set ukp own environ in terminal
use venv to activate

venv stelios1 activate
source stelios1/bin/activate
deactivate

always create an environment for your folder

means you have a stable and reproducible environment.

nb can go to mt % history t osee what have already run.
'''