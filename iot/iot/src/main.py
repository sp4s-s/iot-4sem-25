import subprocess

def run_attendance():
    try:
        print("\n[Running f1.py]")
        subprocess.run(["python", "f1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[Error] file1.py exited with code {e.returncode}")
    except FileNotFoundError:
        print("[Error] file1.py not found")

def run_temperature():
    try:
        print("\n[Running file2.py]")
        subprocess.run(["python", "dht1.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[Error] file2.py exited with code {e.returncode}")
    except FileNotFoundError:
        print("[Error] file2.py not found")

def run_ir_sanitizer():
    try:
        print("\n[Running file3.sh]")
        subprocess.run(["bash", "irsen.sh"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[Error] file3.sh exited with code {e.returncode}")
    except FileNotFoundError:
        print("[Error] file3.sh not found or not executable")

def show_menu():
    print("\n")
    print("1. Run Attendance (file1.py)")
    print("2. Get Temperature (file2.py)")
    print("3. Activate IR Sanitizer (file3.sh)")
    print("q. Quit")

def main():
    while True:
        show_menu()
        choice = input("> ").strip()

        if choice.lower() == "q":
            print("Goodbye.")
            break
        elif choice == "1":
            run_attendance()
        elif choice == "2":
            run_temperature()
        elif choice == "3":
            run_ir_sanitizer()
        else:
            print("Invalid input. Please enter 1, 2, 3, or q.")

if __name__ == "__main__":
    main()
