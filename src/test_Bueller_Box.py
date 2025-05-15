"""
test_Bueller_Box.py
-------------------
Consolidated test runner for Bueller Box modules.

Usage:
    python test_Bueller_Box.py --mode slides_metadata
    python test_Bueller_Box.py --mode slides_capture
    python test_Bueller_Box.py --mode kaltura_download
    python test_Bueller_Box.py --mode canvas_scrape
    python test_Bueller_Box.py --mode bookmarks
"""

import os
import argparse
import logging
import json

from slides_capturer import get_slide_metadata, capture_slides
from canvas_scraper import extract_from_canvas_page
# from kaltura_downloader import download_kaltura_video
from bookmark_loader_v2 import load_all_bookmarks

# Ensure test_exports directory and logging setup
output_dir = os.path.join(os.getcwd(), "test_exports")
os.makedirs(output_dir, exist_ok=True)

log_path = os.path.join(output_dir, "log.txt")
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_slide_metadata_test():
    test_url = "https://docs.google.com/presentation/d/1jRs7QULaSJYF4fNC0a7-l7pvjA-0xo_G/edit?usp=sharing"
    print("🔍 Running Slide Metadata Test...")
    logging.info("Running Slide Metadata Test...")
    metadata = get_slide_metadata(test_url)
    logging.info(f"Metadata: {metadata}")
    print("🔍 Slide Metadata Result:")
    print(metadata)

def run_slide_capture_test():
    test_url = "https://docs.google.com/presentation/d/1jRs7QULaSJYF4fNC0a7-l7pvjA-0xo_G/edit?usp=sharing"
    print("🖼️ Running Full Slide Capture Test...")
    logging.info("Running Full Slide Capture Test...")
    capture_slides(test_url, output_dir)
    logging.info(f"Slide capture saved to: {output_dir}")

def run_kaltura_test():
    test_url = "https://your-kaltura-link.com"
    print("🎥 Running Kaltura Download Test...")
    logging.info("Running Kaltura Download Test...")
    # download_kaltura_video(test_url, output_dir)
    logging.info("Kaltura download stub executed.")

def run_canvas_scrape_test():
    test_url = "https://digitalskills.instructure.com/courses/13415/pages/1-dot-2-%7C-live-class-presentations?module_item_id=1924184"
    print("🧠 Running Canvas LMS Page Scrape...")
    logging.info("Running Canvas LMS Page Scrape...")
    extract_from_canvas_page(test_url, output_dir)

def run_bookmark_test():
    print("🔖 Running Chrome Bookmark Loader Test...")
    logging.info("Running Bookmark Loader Test...")
    bookmarks = load_all_bookmarks()
    logging.info(f"Loaded {len(bookmarks)} bookmarks.")
    with open(os.path.join(output_dir, "bookmarks.json"), "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, indent=2)
    print(f"📥 Saved merged bookmarks to {output_dir}/bookmarks.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bueller Box Test Runner")
    parser.add_argument("--mode", type=str, required=True,
                        choices=["slides_metadata", "slides_capture", "kaltura_download", "canvas_scrape", "bookmarks"],
                        help="Choose the test mode to run.")
    args = parser.parse_args()

    if args.mode == "slides_metadata":
        run_slide_metadata_test()
    elif args.mode == "slides_capture":
        run_slide_capture_test()
    elif args.mode == "kaltura_download":
        run_kaltura_test()
    elif args.mode == "canvas_scrape":
        run_canvas_scrape_test()
    elif args.mode == "bookmarks":
        run_bookmark_test()
