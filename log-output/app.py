import time
import uuid
from datetime import datetime

def main():
    random_string = str(uuid.uuid4())
    print(f"Application started with ID: {random_string}")

    while True:
        timestamp = datetime.utcnow().isoformat() + "Z"
        print(f"{timestamp}: {random_string}", flush=True)
        time.sleep(5)

if __name__ == "__main__":
    main()
