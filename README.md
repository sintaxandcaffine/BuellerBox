# 📦 Bueller Box - Nerdvana Lecture Lifter Module

Welcome to **Bueller Box**, the retro-fueled lecture media collector from the Nerdvana suite. This is the ultimate WinAmp-style academic mixtape builder for the curious, the nostalgic, and the always-late-to-class.

---

## 📁 Repository Structure

```
BuellerBox/
├── .gitignore
├── LICENSE
├── LICENSE.md
├── PROJECT_LOG_BuellerBox.md
├── README.md
├── requirements.txt
├── assets/
│   ├── bueller_box_favicon_refined.png
│   ├── bueller_box_github.png
│   └── bueller_box_stamped.png
├── chat_logs/
│   └── nerdvana_it_awakens_migration.md
├── dev_log/
│   └── PROJECT_LOG.md
├── docs/
│   └── overview.md
├── exts/
│   ├── background.js
│   └── manifest.json
├── src/
│   ├── __init__.py
│   ├── bookmark_loader_v2.py
│   ├── bueller_launcher.py
│   ├── bueller_passive_mode.py
│   ├── canvas_scraper.py
│   ├── kaltura_downloader.py
│   ├── selector_ui.py
│   ├── slides_capturer.py
│   ├── tab_bridge_listener.py
│   ├── tab_handler.py
│   ├── tab_logs/
│   ├── tab_scanner.py
│   ├── test_Bueller_Box.py
│   ├── test_exports/
│   └── utils.py
├── venv/
```

---

## 🎯 Module Purpose
**Bueller Box** is a standalone module in the Nerd-Army-Calculator built to:
- Capture and organize Google Slides, Kaltura videos, and lecture-related assets
- Archive transcripts, attachments, and metadata
- Store everything locally or sync to a structured Nerdvana cloud vault
- Scrape entire Canvas pages for all embedded lecture content
- Passively detect browser tabs (via Chrome debug mode or extension) and allow tab selection via checkbox UI
- Aggregate bookmarks from all Chrome profiles without sign-in
- Use a debug-enabled Chrome browser or extension-based bridge as its GUI shell
- Eventually extract data behind graphs and charts into spreadsheet format

---

## 💾 Current Features
- [x] Google Slides Capturer (metadata + PDF export working!)
- [ ] Kaltura Downloader (stub scaffolded)
- [x] Canvas Page Scraper (multi-slide deck detection)
- [x] Bookmark Loader (multi-profile, deduplicated)
- [x] Passive Mode: Detect and select Chrome tabs via UI
- [x] Chrome Debug Launcher simulating guest mode
- [x] Tab Handler with routing logic
- [x] Tab Selector UI via customtkinter
- [x] Chrome Extension Bridge for real-time tab fetching
- [x] Flask Listener to receive tab data (`tab_bridge_listener.py`)
- [ ] Reverse Graph/Data Extraction (planned)
- [ ] Flask-based interface under construction

---

## 🚧 Dev Notes
- ✅ Created and tested `tab_bridge_listener.py`, receiving tab data via POST and logging it to /tab_logs/
- ✅ Validated Chrome Extension communication via `fetch()` and `chrome.tabs.query()`
- ✅ Resolved extension background execution context issues
- ✅ Verified full tab relay from Chrome to Python listener
- ✅ Prepared plan for integration with Passive Mode selector UI using logged tabs
- ✅ Will next parse latest tab JSON file and auto-feed into selector for user confirmation
- ✅ Updated repository structure to reflect real folder layout including `exts/`, `venv/`, `tab_logs/`, and `test_exports/`

---

## 🧪 Tests Logged
- 🧪 Manual background script execution via Chrome service worker DevTools
- 🧪 Chrome tab sync triggered using `chrome.runtime.sendMessage` in extension context
- 🧪 Verified Flask endpoint received and logged tab data to file
- 🧪 Confirmed cross-component bridge from background.js → fetch → Flask → JSON output

---

## 🐞 Known Issues / Fixes
- ⚠️ `chrome.runtime.sendMessage` fails if called inside its own background context
  - ✅ Resolved by triggering from valid runtime context (popup or manual query injection)
- ⚠️ No handler defined for `localhost` tabs (dev server tabs mistakenly selected)
  - ✅ Excluded from selector UI routing
- ⚠️ `flask` module not found when running `tab_bridge_listener.py`
  - ✅ Fixed by installing Flask with `pip install flask`
- ⚠️ Service Worker showed inactive; logs hidden in extension
  - ✅ Switched to correct DevTools context → forced manual trigger via `fetch()` test

---

## 🕹️ Retro Goals
> "Life moves pretty fast. If you don’t stop and capture your lectures once in a while, you could miss it."

Let the lecture lifting begin.

> *Module powered by SinTaxAndCaffeine – For Nerds Who Never Skip Class.*
