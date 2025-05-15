"""
bookmark_loader_v2.py
---------------------
Scans all Chrome profile folders for bookmarks, deduplicates by URL,
and outputs a unified JSON list.

Author: SinTaxAndCaffeine
"""

import os
import json
import glob

def get_user_bookmark_paths():
    base_path = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")
    pattern = os.path.join(base_path, "Profile *", "Bookmarks")
    return glob.glob(pattern)

def load_all_bookmarks():
    bookmark_paths = get_user_bookmark_paths()
    bookmarks = []
    seen_urls = set()

    def extract_bookmarks(node):
        if node.get("type") == "url":
            url = node.get("url")
            if url not in seen_urls:
                bookmarks.append({
                    "name": node.get("name"),
                    "url": url
                })
                seen_urls.add(url)
        elif node.get("type") == "folder":
            for child in node.get("children", []):
                extract_bookmarks(child)

    for path in bookmark_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            roots = data.get("roots", {})
            for section in ["bookmark_bar", "other", "synced"]:
                if section in roots:
                    extract_bookmarks(roots[section])
        except Exception as e:
            print(f"⚠️ Skipped {path}: {e}")

    return bookmarks

if __name__ == "__main__":
    try:
        all_bm = load_all_bookmarks()
        print(json.dumps(all_bm, indent=2))
    except Exception as e:
        print(f"❌ Error loading bookmarks: {e}")
