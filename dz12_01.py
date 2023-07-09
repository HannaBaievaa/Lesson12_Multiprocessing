#імпорт класу  TPE  із пакету СЕ(пакет для асинхронного виконання програм із використанням
# потоків ThreadPoolExecutor або процесів ProcessPoolExecutor)

from concurrent.futures import ThreadPoolExecutor
import time

# функція, що обраховує факторіал числа
def factorial_function(s) :
    if s == 0 or s  == 1 :
        return 1
    else :
        return s*factorial_function(s-1)
print(factorial_function(6))

#стандартний оберт, точка входу в процедуру
#засічка часу
#створення пулів із 3-х потоків
#вивід результатів вимірювання швидкості обчислень

if __name__ == '__main__':
    print("Starting TreadPoolExecutor")
    with ThreadPoolExecutor(max_workers=3) as ex :
        starter_at = time.time()
        val = ex.submit(factorial_function(2))
        val = ex.submit(factorial_function(4))
        val = ex.submit(factorial_function(5))
        print("All the threads are processed completely")
        print(f"Time: {time.time() - starter_at}")








