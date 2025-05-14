"""
utils.py
--------
Shared utility functions for Bueller Box.

Author: SinTaxAndCaffeine
"""

import os
import logging

logger = logging.getLogger(__name__)

def ensure_output_dir(path: str):
    """
    Ensures the output directory exists.

    Args:
        path (str): The path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        logger.debug(f"Created output directory at: {path}")
    else:
        logger.debug(f"Output directory already exists: {path}")
