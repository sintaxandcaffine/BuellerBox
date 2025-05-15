"""
bueller_launcher.py
-------------------
Launches Chrome in remote debugging mode using a clean user profile
(simulates guest mode) and prepares Bueller Passive Mode.

Author: SinTaxAndCaffeine
"""

import subprocess
import os
import time
import webbrowser
import requests
import sys
import signal

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DEBUG_PORT = "9222"
USER_DATA_DIR = r"C:\Temp\BuellerGuest"
UI_URL = "http://localhost:5000"  # Placeholder for future Bueller GUI
TEST_JSON_ENDPOINT = f"http://localhost:{DEBUG_PORT}/json"

def close_existing_chrome():
    try:
        subprocess.call("taskkill /f /im chrome.exe", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("🛑 Closed existing Chrome instances.")
    except Exception as e:
        print(f"⚠️ Could not close Chrome automatically: {e}")

def launch_chrome_debug():
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)
    print("🚀 Launching Chrome in debug mode...")
    subprocess.Popen([
        CHROME_PATH,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={USER_DATA_DIR}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--disable-popup-blocking",
        "--new-window",
        UI_URL  # Load future Bueller UI automatically
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def wait_for_debugger(timeout=10):
    print("🔍 Waiting for Chrome debugger to become available...")
    for _ in range(timeout * 2):
        try:
            res = requests.get(TEST_JSON_ENDPOINT)
            if res.status_code == 200:
                print("✅ Chrome debug mode is live.")
                return True
        except:
            pass
        time.sleep(0.5)
    print("❌ Failed to connect to Chrome debugger.")
    return False

if __name__ == "__main__":
    close_existing_chrome()
    launch_chrome_debug()
    if not wait_for_debugger():
        print("💡 Tip: Make sure Chrome is installed at the expected path and not blocked by antivirus.")
        sys.exit(1)

    print("💡 You may now open tabs in Chrome. Bueller will scan them shortly.")
