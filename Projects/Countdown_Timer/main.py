import time
import os
import threading
import keyboard  # install this via: pip install keyboard

exit_flag = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def check_for_enter():
    global exit_flag
    keyboard.read_event()
    exit_flag = True

def countdown_timer(total_seconds):
    global exit_flag
    try:
        while total_seconds and not exit_flag:
            clear_console()
            print("⏳ Countdown Timer (press Enter to stop)")
            print("--------------------")
            print("Time Left:", format_time(total_seconds))
            time.sleep(1)
            total_seconds -= 1

        clear_console()
        if exit_flag:
            print("⛔ Timer stopped by user.")
        else:
            print("⏰ Time's up!")
    except KeyboardInterrupt:
        print("\n⛔ Timer interrupted manually.")

if __name__ == "__main__":
    print("🔢 Enter countdown time:")
    try:
        hrs = int(input("Hours: ") or 0)
        mins = int(input("Minutes: ") or 0)
        secs = int(input("Seconds: ") or 0)

        total = hrs * 3600 + mins * 60 + secs
        if total <= 0:
            print("❗ Please enter a valid time greater than 0.")
        else:
            # Start input-listener thread
            listener_thread = threading.Thread(target=check_for_enter, daemon=True)
            listener_thread.start()
            
            countdown_timer(total)

    except ValueError:
        print("⚠️ Invalid input! Please enter numeric values only.")
