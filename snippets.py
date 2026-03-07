import json
import os

DB_FILE = "my_snippets.json"

def save_snippet(name, code):
    data = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
    
    data[name] = code
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ Snippet '{name}' saved successfully!")

def get_snippet(name):
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
            return data.get(name, "❌ Snippet nahi mila!")
    return "❌ Database empty hai!"

if __name__ == "__main__":
    choice = input("Kya karna hai? (1: Save, 2: Get): ")
    if choice == '1':
        name = input("Snippet ka naam: ")
        code = input("Code yahan paste karein: ")
        save_snippet(name, code)
    elif choice == '2':
        name = input("Kaunsa snippet chahiye?: ")
        print("\n--- Aapka Code ---\n", get_snippet(name))
