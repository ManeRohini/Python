"""
3: Design a Python application where multiple threads update a shared variable.

Use a Lock to avoid race conditions.

Each thread should increment the shared counter multiple times.

Display the final value of the counter after all threads complete execution.
"""
import threading

counter = 0          # shared variable
lock = threading.Lock()

def worker():
    global counter
    for _ in range(1000):   # each thread increments 1000 times
        with lock:          # lock ensures safe update
            counter += 1

def main():
    threads = []
    for _ in range(5):      # create 5 threads
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
