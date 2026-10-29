# College Help Desk

A website for college info (Teachers, Transport, Library, Labs, Canteen).
Built only with **Python (Flask)**, **MySQL**, **HTML** and **CSS** — no JavaScript.

## Run it
1. Install packages: `pip install flask mysql-connector-python`
2. Create the database: open MySQL and run `SOURCE schema.sql;`
3. In `app.py`, put your MySQL password in the `DB` line.
4. Start: `python app.py` → open http://127.0.0.1:5000

## Features
- Home page search across all 5 tables at once
- One page per table with search, add and delete
- Status tags (Available / Issued / Free / Booked)

## Files
```
app.py            Python backend (routes + MySQL queries)
schema.sql        Tables + sample data
templates/        HTML pages
static/style.css  Styling
```
