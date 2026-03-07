import datetime

def generate_report():
    day = "Day 13"
    print(f"--- {day} Reporting System ---")
    
    # User se info lena
    projects_done = input("Aaj kaun-kaun se projects banaye? (Comma se separate karein): ")
    learning = input("Aaj sabse badi seekh kya thi?: ")
    
    # Report ka format
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_content = f"""
---------------------------------------
📅 Date: {timestamp} | {day}
🚀 Projects: {projects_done}
🧠 Key Learning: {learning}
✅ Status: Mission Accomplished!
---------------------------------------
\n"""

    # File mein save karna (Append mode 'a' use kiya hai taaki purana delete na ho)
    with open("Daily_Report.txt", "a") as file:
        file.write(report_content)
    
    print("\n🎉 Report generated and saved in 'Daily_Report.txt'!")

if __name__ == "__main__":
    generate_report()
