<p align="center">
  <img src="assets/bueller_box_github.png" alt="Bueller Box Logo" width="320"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/repo-size/sintaxandcaffine/BuellerBox" alt="Repo Size"/>
  <img src="https://img.shields.io/github/commit-activity/m/sintaxandcaffine/BuellerBox" alt="Commit Activity"/>
  <img src="https://img.shields.io/github/last-commit/sintaxandcaffine/BuellerBox" alt="Last Commit"/>
  <img src="https://img.shields.io/github/issues/sintaxandcaffine/BuellerBox" alt="Open Issues"/>
  <img src="https://img.shields.io/github/license/sintaxandcaffine/BuellerBox" alt="License"/>
  <img src="https://img.shields.io/badge/built%20with-Python%203.10+-blue?logo=python" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Nerdvana-Approved%20Tool-ff69b4?style=flat-square&logo=data:image/svg+xml;base64,SGVyZSdzIHdoZXJlIHRoZSBuZXJkcyBzaXQ=" alt="Nerdvana Approved"/>
</p>

# 📦 Bueller Box - Nerdvana Lecture Lifter Module

Welcome to **Bueller Box**, the retro-fueled lecture media collector from the Nerdvana suite. This is the ultimate WinAmp-style academic mixtape builder for the curious, the nostalgic, and the always-late-to-class.

---

## 📁 Repository Structure

```
BuellerBox/
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── assets/
│   ├── bueller_box_github.png
│   ├── bueller_box_favicon_refined.png
│   └── bueller_box_stamped.png
├── docs/
│   └── overview.md
├── chat_logs/
│   └── nerdvana_it_awakens_migration.md
├── dev_log/
│   └── PROJECT_LOG.md
├── src/
│   ├── __init__.py
│   ├── kaltura_downloader.py
│   ├── slides_capturer.py├── canvas_scraper.py
│   └── utils.py
├── bookmark_loader_v2.py
├── bueller_launcher.py
└── test_Bueller_Box.py
```

---

## 🎯 Module Purpose
**Bueller Box** is a standalone module in the Nerd-Army-Calculator built to:
- Capture and organize Google Slides, Kaltura videos, and lecture-related assets
- Archive transcripts, attachments, and metadata
- Store everything locally or sync to a structured Nerdvana cloud vault
- Scrape entire Canvas pages for all embedded lecture content
- Passively detect browser tabs (via Chrome debug mode) and let users select what tabs to capture via checkbox UI
- Aggregate and surface bookmarks, without sign-in, from all Chrome profiles for fast access 
- Use a debug-enabled Chrome browser as its GUI shell
- Eventually extract data behind graphs and charts into spreadsheet format
---

## 💾 Current Features
- [x] Google Slides Capturer (metadata + PDF export working!)
- [ ] Kaltura Downloader (stub scaffolded)
- [ ] Lecture Timeline Annotator (TBD)
- [ ] Transcript & Attachment Organizer
- [ ] Retro-themed GUI w/ nostalgic skins
- [x] Canvas Page Scraper (multi-slide deck detection)
- [x] Bookmark Loader (multi-profile, deduplicated)
- [ ] Reverse Graph/Data Extraction (planned)
- [x] CLI-based unified test runner with logging
- [x] Chrome Guest Mode Launcher with debugging enabled
- [x] Passive Mode: Chrome Tab Inspector and tab Selector UI
- [ ] Pop-out Bookmark Panel in GUI
- [ ] Flask-based interface under construction

---

## 🧪 Testing Usage

```bash
python test_Bueller_Box.py --mode slides_metadata
python test_Bueller_Box.py --mode canvas_scrape
python test_Bueller_Box.py --mode bookmarks
```

---

## 🔧 Setup
```bash
# Clone the repo
$ git clone https://github.com/SinTaxAndCaffeine/BuellerBox.git
$ cd BuellerBox

# Set up environment (Python 3.10+)
$ python -m venv venv
$ .\venv\Scripts\activate  # On Windows
$ pip install -r requirements.txt
```

---

## 🛠️ Dev Utilities

- `bueller_launcher.py` — Launches Chrome with debug port in guest-style profile
- `bookmark_loader_v2.py` — Collects bookmarks from all `Profile *` folders
- `tab_scanner.py` — Lists Chrome tabs via remote debugging
- `selector_ui.py` — Presents checkbox GUI for selecting tabs
- `tab_handler.py` — Routes selected tabs to scraping tools

---

## 🚧 Dev Notes
- Created and verified `bookmark_loader_v2.py` to pull bookmarks from all Chrome profiles (Profile 1–5)
- Deduplicates bookmarks by URL and saves as `bookmarks.json` in `/test_exports`
- Integrated bookmark test mode into universal CLI tester
- Developed `bueller_launcher.py` to launch Chrome in simulated guest mode with remote debugging
- Successfully verified Chrome debugger activation at `localhost:9222/json`
- Confirmed `canvas_scraper.py` pulls all embedded Google Slides from public LMS pages
- Outlined architecture for GUI in debug-mode Chrome (Flask frontend + tab scraping)
- Updated universal tester to support `--mode bookmarks`
- Documented user Chrome launch expectations and fallback UX when debugger not detected
- Prepped future plan to load bookmarks in GUI pop-out panel from `bookmarks.json`
- Bookmarks extracted via wildcard glob across all profile folders
- Initial module stubs created for `kaltura_downloader.py`, `slides_capturer.py`, and `utils.py`
- Built and verified `get_slide_metadata()` and `capture_slides()` with PDF export
- Added CLI-based test runner via `test_Bueller_Box.py`
- Enabled log saving to `test_exports/log.txt`
- Confirmed valid published Google Slides format required for metadata extraction

---

## 🐞 Known Issues / Fixes
- ⚠️ Bookmarks file not found if only checking `Default` profile
  - ✅ Fixed by scanning all `Profile *` folders using wildcard + glob
- ⚠️ Chrome must be launched in debug mode for Passive Tab Detection
  - ✅ Bueller attempts auto-launch via `bueller_launcher.py`, offers fallback if Chrome is open
- ⚠️ Chrome opened with missing page at `localhost:5000`
  - ✅ Expected; placeholder for future Flask GUI
- ⚠️ Sign-in prompt avoidance desired during debug-mode launch
  - ✅ Resolved using isolated `--user-data-dir` to simulate guest session
- ⚠️ **Invalid Slide URLs**: Private/unpublished links return "Page Not Found"
  - ✅ Solution: Use "Publish to web" versions or ensure "Anyone with link can view"
- 🧠 **User error with unquoted URLs** caused early syntax error in test file
  - ✅ Resolved by wrapping the URL in quotes (Python string syntax)
- 🧪 Some Google Slides URLs don't return actual title unless published or accessible without login
  - ✅ Added fallback logic and testing URLs
  - ✅ Bookmarks resolved using wildcard profile scanner
  - ✅ Passive Chrome UI opens even if user not signed in
  - ✅ Launcher attempts to close existing Chrome instances gracefully
  - ⚠️ Missing Flask GUI at `localhost:5000` — expected

---

## 🕹️ Retro Goals
> "Life moves pretty fast. If you don’t stop and capture your lectures once in a while, you could miss it."

Let the lecture lifting begin.

> *Module powered by SinTaxAndCaffeine – For Nerds Who Never Skip Class.*
