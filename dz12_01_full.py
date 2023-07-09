from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def factorial_function(s) :
    if s == 0 or s  == 1 :
        return 1
    else :
        return s*factorial_function(s-1)

if __name__ == '__main__':
    print("Starting TreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as ex :
        starter_at = time.time()
        val = ex.submit(factorial_function(2))
        val = ex.submit(factorial_function(4))
        val = ex.submit(factorial_function(5))
        print("All the threads are processed completely")
        time1 = time.time() - starter_at
        print(f"Time 1:", {time1})

    print("*"*33)
    print("Starting ProcessPoolExecutor")
    with ProcessPoolExecutor(max_workers=3) as z:
        starter_at = time.time()
        val = z.submit(factorial_function(2))
        val = z.submit(factorial_function(4))
        val = z.submit(factorial_function(5))
        print("All processes are completely")
        time2 = time.time() - starter_at
        print(f"Time 2:", {time2})

    print("*" * 33)


    if time1 > time2 :
        print(f"Best method is ThreadPoolExecutor!, time: {time1}")
    else:
        print(f"Best method is ProcessPoolExecutor!, time: {time2}")
