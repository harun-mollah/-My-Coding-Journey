import json
from datetime import datetime
import os

def update_streak(task_name):
    filename = 'coding_log.json'
    today = str(datetime.now().date())
    
    # Check if file exists
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    # Update data
    data[today] = task_name
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"✅ Awesome! Day {len(data)} logged: {task_name}")
    print("Welcome back! Your consistency is building up again. 🚀")

# Run the tracker
if __name__ == "__main__":
    my_task = input("Aaj kya seekha? (Type here): ")
    update_streak(my_task)
