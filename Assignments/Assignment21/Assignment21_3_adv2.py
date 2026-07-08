"""
3: Design a Python application where multiple threads update a shared variable.

Use a Lock to avoid race conditions.

Each thread should increment the shared counter multiple times.

Display the final value of the counter after all threads complete execution.
"""
import threading

# Shared variable
counter = 0

# Create a Lock object
lock = threading.Lock()

def increment_counter(times):
    global counter
    for _ in range(times):
        # Acquire lock before updating shared variable
        with lock:
            counter += 1

def main():
    threads = []
    num_threads = 5       # number of threads
    increments_per_thread = 1000  # how many times each thread increments

    # Create threads
    for i in range(num_threads):
        t = threading.Thread(target=increment_counter, args=(increments_per_thread,), name=f"Thread-{i+1}")
        threads.append(t)

    # Start threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Final counter value:", counter)
    print("Exit from main")

if __name__ == "__main__":
    main()
