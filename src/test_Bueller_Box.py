"""
test_Bueller_Box.py
-------------------
Consolidated test runner for Bueller Box modules.

Usage:
    python test_Bueller_Box.py --mode slides_metadata
    python test_Bueller_Box.py --mode slides_capture
    python test_Bueller_Box.py --mode kaltura_download
"""

import os
import argparse
import logging
from slides_capturer import get_slide_metadata, capture_slides
# from kaltura_downloader import download_kaltura_video

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bueller Box Test Runner")
    parser.add_argument("--mode", type=str, required=True,
                        choices=["slides_metadata", "slides_capture", "kaltura_download"],
                        help="Choose the test mode to run.")
    args = parser.parse_args()

    if args.mode == "slides_metadata":
        run_slide_metadata_test()
    elif args.mode == "slides_capture":
        run_slide_capture_test()
    elif args.mode == "kaltura_download":
        run_kaltura_test()
