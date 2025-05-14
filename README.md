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
│   ├── slides_capturer.py
│   └── utils.py
└── test_Bueller_Box.py
```

---

## 🎯 Module Purpose
**Bueller Box** is a standalone module in the Nerd-Army-Calculator built to:
- Capture and organize Google Slides, Kaltura videos, and lecture-related assets
- Archive transcripts, attachments, and metadata
- Store everything locally or sync to a structured Nerdvana cloud vault

---

## 💾 Current Features
- [x] Google Slides Capturer (metadata + PDF export working!)
- [ ] Kaltura Downloader (stub scaffolded)
- [ ] Lecture Timeline Annotator (TBD)
- [ ] Transcript & Attachment Organizer
- [ ] Retro-themed GUI w/ nostalgic skins
- [x] CLI-based unified test runner with logging

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

## 🚧 Dev Notes
- Initial module stubs created for `kaltura_downloader.py`, `slides_capturer.py`, and `utils.py`
- Built and verified `get_slide_metadata()` and `capture_slides()` with PDF export
- Added CLI-based test runner via `test_Bueller_Box.py`
- Enabled log saving to `test_exports/log.txt`
- Confirmed valid published Google Slides format required for metadata extraction

---

## 🐞 Known Issues / Fixes
- ⚠️ **Invalid Slide URLs**: Private/unpublished links return "Page Not Found"
  - ✅ Solution: Use "Publish to web" versions or ensure "Anyone with link can view"
- 🧠 **User error with unquoted URLs** caused early syntax error in test file
  - ✅ Resolved by wrapping the URL in quotes (Python string syntax)
- 🧪 Some Google Slides URLs don't return actual title unless published or accessible without login
  - ✅ Added fallback logic and testing URLs

---

## 🕹️ Retro Goals
> "Life moves pretty fast. If you don’t stop and capture your lectures once in a while, you could miss it."

Let the lecture lifting begin.

> *Module powered by SinTaxAndCaffeine – For Nerds Who Never Skip Class.*
