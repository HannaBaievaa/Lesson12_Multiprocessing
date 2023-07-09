#імпоруємо необхідні бібліотеки
import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, waiting numbers')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)

    #пишемо одну загальну функцію з 3-ма процессами та розтавляємо пріорітети
    async def our_functions(a,b):
        print(f'Додавання: {a+ b}')
        await asyncio.sleep(0)
        print(f'Віднімання: {a - b}')
        await asyncio.sleep(1)
        print(f'Множення: {a * b}')
        await asyncio.sleep(3)

    #виклик асинхронноі функціі та виклик корутини
    coroutine = our_functions()

    #відправляємо оброблені дані клієнту та закриваємо з'єднання
    conn.send(coroutine.send(None))
    conn.close()


