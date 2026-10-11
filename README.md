# Scholarship Deadline Tracker

A Python application for tracking scholarship deadlines, requirements, and application progress in one place.

## Why I built this

While researching scholarships for my own studies, I kept running into the same problem: opportunities were scattered across dozens of websites, with no single place to track deadlines, requirements, or application status. I built this tool to solve that problem directly — and to deepen my practical skills in Python, data handling, and deployment by building something genuinely useful rather than following a tutorial.

## What it does

- **Track scholarships** — university, country, scholarship type, deadline, application fee, and required documents, all in one place
- **Automatic urgency calculation** — see at a glance how many days remain until each deadline
- **Sort by urgency** — the most time-sensitive applications always surface first
- **Dual interface** — a command-line tool for quick local use, and a deployed web app for anywhere access
- **Status tracking** — follow each application's progress through its lifecycle

## Try it live

**[scholarship-deadline-tracker-doris.streamlit.app](https://scholarship-deadline-tracker-doris.streamlit.app)**

## Tech stack

- **Python** — core application logic
- **Streamlit** — web interface and deployment
- **pandas** — data processing, sorting, and transformation
- **CSV** — data storage
- **Git/GitHub** — version control and collaboration workflow

## How to run it locally

```bash
git clone https://github.com/duchessdoriano/Scholarship-deadline-tracker.git
cd Scholarship-deadline-tracker
pip install -r requirements.txt

# Command-line version
python tracker.py

# Web app version
streamlit run app.py
```

## What this project strengthened

Building and deploying this end-to-end gave me hands-on experience with:

- Structuring an application around clean, reusable functions
- Working with structured data (CSV) and handling edge cases — e.g. unescaped delimiters breaking column alignment
- Data manipulation and transformation with pandas, including date arithmetic and sorting
- Building an interactive UI with Streamlit, including forms and state handling
- A full Git/GitHub workflow — commits, remote syncing, and managing a project's history
- Deploying a Python application to a public, production environment

## Roadmap

This is Version 1, built as a functional foundation. Planned next steps:

- [ ] Input validation and error handling
- [ ] Expanded status pipeline (Researching → Documents Pending → Ready to Apply → Applied → Accepted/Rejected)
- [ ] Color-coded urgency indicators
- [ ] Search and filtering (by country, type, status, deadline range)
- [ ] Dashboard summary view
- [ ] Per-scholarship document checklists
- [ ] Modular code architecture (separating interface, data layer, and business logic)

Longer-term, I'm interested in exploring a recommendation feature that surfaces relevant scholarships based on a user's profile — a natural extension once the current architecture is more modular.
