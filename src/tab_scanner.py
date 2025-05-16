"""
tab_scanner.py
--------------
Connects to Chrome's remote debugger and lists open tabs.

Author: SinTaxAndCaffeine
"""

import requests

DEBUG_PORT = "9222"
CHROME_ENDPOINT = f"http://localhost:{DEBUG_PORT}/json"

def get_open_tabs():
    try:
        response = requests.get(CHROME_ENDPOINT)
        response.raise_for_status()
        tabs = response.json()
        return [{
            "title": tab.get("title"),
            "url": tab.get("url")
        } for tab in tabs if "http" in tab.get("url", "") and "chrome://" not in tab.get("url", "")]
    except Exception as e:
        print(f"❌ Error connecting to Chrome debug port: {e}")
        return []

if __name__ == "__main__":
    open_tabs = get_open_tabs()
    for i, tab in enumerate(open_tabs, 1):
        print(f"{i}. {tab['title']} - {tab['url']}")
