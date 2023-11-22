import schedule
import time
from datetime import datetime
from subprocess import run

def run_main():
    print(f"Running main.py at {datetime.now()}")
    run(["python", "main.py"])

schedule.every().hour.do(run_main)

while True:
    schedule.run_pending()
    time.sleep(1)
