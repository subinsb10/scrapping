from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"\n🔁 Detected change in: {event.src_path}")
            print("▶️ Restarting script...\n")
            subprocess.run(["python", "app.py"])

if __name__ == "__main__":
    path = "."
    print("👀 Watching for changes in Python files...")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
