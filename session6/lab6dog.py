import requests, os

def fetch_and_save_dog_image(index):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()['message']
        print(f"[{index}] Downloading 🐕: {image_url}")

        # Extract filename from URL
        filename = f"{index}_" + os.path.basename(image_url)

        # Download the image content
        image_data = requests.get(image_url).content

        # Save to file
        with open(filename, 'wb') as file:
            file.write(image_data)

        print(f"[{index}] Image saved as: {filename}")
    else:
        print(f"[{index}] Failed to fetch dog image.")

if __name__ == "__main__":
    fetch_and_save_dog_image(0)


#  if can do this for one, can do this in parallel. Task 1 is to download 4 photos with serial runner and note time.
#  Task 2 is to download 4 photos with parallel runner and note time.

import time

# Serial runner - dog images
def serial_runner_dog():
    start = time.perf_counter()
    for i in range(4):
        fetch_and_save_dog_image(i)
    
    end = time.perf_counter()
    return end - start

# Parallel thread runner
import concurrent.futures
def parallel_runner_dog(index):  # secs is a list [0,1,2,3]
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(fetch_and_save_dog_image,index)

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    print("Serial", serial_runner_dog())
    print("Parallel", parallel_runner_dog([0,1,2,3]))


#Task 3 - download only 2 photos at a time, using semaphore.

import threading, requests, os, time

semaphore = threading.Semaphore(2)   # this is where we are limiting to 2 at a time.

'''def fetch_and_save_dog_image_semaphore(index, semaphore):  #  no need for this, do it in the parallel runner function
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        image_url = response.json()['message']
        print(f"[{index}] Downloading 🐕: {image_url}")

        # Extract filename from URL
        filename = f"{index}_" + os.path.basename(image_url)

        # Download the image content

        semaphore.acquire()
        print("Acquired")

        image_data = requests.get(image_url).content

        # Save to file
        with open(filename, 'wb') as file:
            file.write(image_data)

        semaphore.release()
        print("Released semaphore")

        print(f"[{index}] Image saved as: {filename}")
    else:
        print(f"[{index}] Failed to fetch dog image.")'''

import requests, os, time

# Parallel thread runner - semaphore
import concurrent.futures, threading, requests, os, time
#from concurrent.futures import semaphore
from concurrent.futures import ThreadPoolExecutor
def parallel_runner_dog_limit2(indexes): 
    start = time.perf_counter()
    # limit  - Semaphore
    semaphore = threading.Semaphore(2)   # this is where we are limiting to 2 at a time.'''


    def limited_fetch(i):
        with semaphore:
            fetch_and_save_dog_image(i)

    with concurrent.futures.ThreadPoolExecutor() as executor:    #  this is a hack so don't need to adjust initial function
                                           #  alternative: could put acquire/release in the main function
        executor.map(limited_fetch, indexes)

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    print("Parallel_semaphore:", parallel_runner_dog_limit2([0,1,2,3]))