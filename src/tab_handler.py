"""
tab_handler.py
--------------
Handles routing of selected Chrome tab URLs into Bueller capture tools.

Author: SinTaxAndCaffeine
"""

from canvas_scraper import extract_from_canvas_page
from slides_capturer import capture_slides
import os

def process_selected_tabs(tabs, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for tab in tabs:
        url = tab["url"]
        print(f"🧠 Processing: {tab['title']} - {url}")
        if "docs.google.com/presentation" in url:
            capture_slides(url, output_dir)
        elif "instructure.com" in url or "canvas" in url:
            extract_from_canvas_page(url, output_dir)
        else:
            print(f"❌ No handler defined for URL: {url}")
