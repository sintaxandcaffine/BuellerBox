"""
bueller_passive_mode.py
-----------------------
Unified launcher for Bueller Passive Mode:
- Scans Chrome tabs via debug port
- Presents checkboxes to select content
- Processes selected tabs using smart routing

Author: SinTaxAndCaffeine
"""

import os
from tab_scanner import get_open_tabs
from selector_ui import prompt_user_to_select_tabs
from tab_handler import process_selected_tabs

def main():
    output_dir = os.path.join(os.getcwd(), "test_exports")
    print("🔍 Scanning Chrome for open tabs...")
    tabs = get_open_tabs()

    if not tabs:
        print("❌ No accessible tabs found. Is Chrome running in debug mode on port 9222?")
        return

    print(f"📑 Found {len(tabs)} tabs. Launching selection window...")
    selected_tabs = prompt_user_to_select_tabs(tabs)

    if not selected_tabs:
        print("🚫 No tabs selected. Exiting.")
        return

    print(f"✅ Processing {len(selected_tabs)} selected tab(s)...")
    process_selected_tabs(selected_tabs, output_dir)
    print("🎉 Bueller Passive Mode complete. All output saved to /test_exports.")

if __name__ == "__main__":
    main()
