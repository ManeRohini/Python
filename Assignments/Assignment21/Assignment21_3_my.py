

import threading

counter = 0
lock = threading.Lock()

def worker(times):
    global counter
    for _ in range(times):
        with lock:   # safe update
            counter += 1

def main():
    t1 = threading.Thread(target=worker, args=(10,))
    t2 = threading.Thread(target=worker, args=(200,))
    t3 = threading.Thread(target=worker, args=(3000,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
