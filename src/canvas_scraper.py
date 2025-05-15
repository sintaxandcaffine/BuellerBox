"""
canvas_scraper.py
-----------------
Parses LMS pages (e.g., Canvas) for embedded lecture media like Google Slides.

Author: SinTaxAndCaffeine
"""

import logging
import requests
from bs4 import BeautifulSoup
from slides_capturer import capture_slides
from utils import ensure_output_dir
import os

logger = logging.getLogger(__name__)

def extract_from_canvas_page(canvas_url: str, output_dir: str):
    """
    Scans a Canvas LMS page for embedded Google Slides and processes them all.

    Args:
        canvas_url (str): The URL to the Canvas LMS content page.
        output_dir (str): Path to save exported files.
    """
    ensure_output_dir(output_dir)

    try:
        logger.info(f"Fetching Canvas page: {canvas_url}")
        response = requests.get(canvas_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all embedded Google Slides presentations
        slides_iframes = soup.find_all("iframe", src=True)
        found = 0

        for iframe in slides_iframes:
            src = iframe["src"]
            if "docs.google.com/presentation" in src:
                found += 1
                logger.info(f"Found Google Slides embed: {src}")
                capture_slides(src, output_dir)

        if found == 0:
            logger.warning("No Google Slides found on this page.")
        else:
            logger.info(f"✅ Successfully captured {found} Google Slides presentations.")

    except Exception as e:
        logger.error(f"Error extracting from Canvas page: {e}")
