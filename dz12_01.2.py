from concurrent.futures import ProcessPoolExecutor
import time

def factorial_function(s) :
    if s == 0 or s  == 1 :
        return 1
    else :
        return s*factorial_function(s-1)
#print(factorial_function(6))

if __name__ == '__main__':
    print("Starting ProcessPoolExecutor")
    with ProcessPoolExecutor(max_workers=3) as z:
        starter_at = time.time()
        val = z.submit(factorial_function(2))
        val = z.submit(factorial_function(4))
        val = z.submit(factorial_function(5))
        print("All processes are completely")
        print(f"Time: {time.time() - starter_at}")
