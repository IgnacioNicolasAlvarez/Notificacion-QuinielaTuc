import schedule
import time
from datetime import datetime
from subprocess import run


def run_main():
    print(f"Running main.py at {datetime.now()}")
    run(["python3", "main.py"])


schedule.every(30).minutes.do(run_main)

while True:
    schedule.run_pending()
    time.sleep(1)
