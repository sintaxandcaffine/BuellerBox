"""
slides_capturer.py
------------------
Module for capturing and processing Google Slides presentations.

Author: SinTaxAndCaffeine
"""

import logging

logger = logging.getLogger(__name__)

def capture_slides(slide_url: str, output_dir: str):
    """
    Main orchestrator function to extract slide metadata and export to PDF.
    
    Args:
        slide_url (str): The URL to the published Google Slides.
        output_dir (str): Path to save the captured slides.
    """
    import os
    from utils import ensure_output_dir

    ensure_output_dir(output_dir)
    metadata = get_slide_metadata(slide_url)
    if not metadata:
        logger.warning("Could not extract metadata. Aborting capture.")
        return

    filename = f"{metadata['title'].replace(' ', '_').replace('/', '-')}.pdf"
    output_path = os.path.join(output_dir, filename)

    export_slides_to_pdf(metadata["presentation_id"], output_path)


def get_slide_metadata(slide_url: str) -> dict:
    """
    Extracts metadata from a public Google Slides URL.

    Args:
        slide_url (str): The URL to the Google Slides presentation.

    Returns:
        dict: Metadata including presentation ID and title (if available).
    """
    import re
    import requests
    from bs4 import BeautifulSoup

    logger.info(f"Parsing slide URL: {slide_url}")

    slide_pattern = r"https://docs\.google\.com/presentation/d/([a-zA-Z0-9-_]+)"
    match = re.search(slide_pattern, slide_url)

    if not match:
        logger.warning("URL does not appear to be a valid Google Slides presentation link.")
        return {}

    presentation_id = match.group(1)

    # Try to fetch the title using BeautifulSoup (if publicly accessible)
    try:
        response = requests.get(slide_url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "Untitled"
    except Exception as e:
        logger.warning(f"Could not fetch presentation title: {e}")
        title = "Untitled"

    return {
        "presentation_id": presentation_id,
        "title": title
    }


def export_slides_to_pdf(presentation_id: str, output_path: str):
    """
    Downloads the full slide deck as a PDF using Google's export endpoint.

    Args:
        presentation_id (str): The extracted Google Slides presentation ID.
        output_path (str): The path where the PDF will be saved.
    """
    import requests

    export_url = f"https://docs.google.com/presentation/d/{presentation_id}/export/pdf"

    try:
        response = requests.get(export_url)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)
        logger.info(f"Slides exported successfully to {output_path}")
    except requests.RequestException as e:
        logger.error(f"Failed to export slides: {e}")
