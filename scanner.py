import os
import re

# Sensitive patterns dhundne ke liye (e.g., API Keys, Passwords)
PATTERNS = {
    "Google API Key": r'AIza[0-9A-Za-z-_]{35}',
    "GitHub Token": r'ghp_[a-zA-Z0-9]{36}',
    "Generic Password": r'password\s*=\s*["\'][^"\']+["\']',
}

def scan_files():
    print("🔍 Scanning your project for leaked secrets...")
    found_issue = False
    
    # Current folder ki saari files check karega
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".js", ".txt", ".env")): # In files ko scan karega
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                    for name, pattern in PATTERNS.items():
                        if re.search(pattern, content):
                            print(f"⚠️  ALERT: {name} found in {path}!")
                            found_issue = True
    
    if not found_issue:
        print("✅ Clean! No obvious secrets found in your code.")

if __name__ == "__main__":
    scan_files()
