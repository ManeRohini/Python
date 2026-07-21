import schedule
import time

def greet():
    print("Good morning, Romo! Task executed successfully.")

# Run every minute
schedule.every(1).minutes.do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)
