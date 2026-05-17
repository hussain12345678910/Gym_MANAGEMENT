# PulseLife Gym — Flask Web Application

A multi-page gym website for **PulseLife Gym**, built with Python Flask. The project serves three pages (Home, About, Membership) using Flask's routing system, Jinja2 templating, and static file handling.

---

## Project Structure

```
pulselife/
├── app.py                  # Flask application & route definitions
├── requirements.txt        # Python dependencies
├── templates/              # Jinja2 HTML templates
│   ├── home.html           # Landing page with hero & features
│   ├── about.html          # About page with team section
│   └── membership.html     # Membership plans & FAQ
└── static/
    └── css/
        └── style.css       # Global stylesheet for all pages
```

---

## Pages & Routes

| Route | Function | Template | Description |
|---|---|---|---|
| `/` | `home()` | `home.html` | Landing page with hero, features, footer |
| `/home` | `home()` | `home.html` | Alias for the home route |
| `/about` | `about()` | `about.html` | About page with team section |
| `/membership` | `membership()` | `membership.html` | Pricing plans and FAQ |

Any unrecognised URL returns the home page with a `404` status code.

---

## Prerequisites

- Python 3.8 or higher
- pip / pip3

---

## Installation & Setup

**1. Clone or download the project**
```bash
cd pulselife
```

**2. (Optional) Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip3 install -r requirements.txt
```

---

## Running the App

```bash
python3 app.py
```

Then open your browser and visit:
```
http://127.0.0.1:5000
```

Flask runs in **debug mode** by default, so the server reloads automatically whenever you save a file.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Backend language |
| Flask 3.x | Web framework & routing |
| Jinja2 | HTML templating (built into Flask) |
| HTML5 | Page structure |
| CSS3 | Styling via `static/css/style.css` |

---

## Key Flask Concepts Used

**`render_template()`** — Renders an HTML file from the `templates/` folder and returns it as the HTTP response.

**`url_for()`** — Generates URLs for routes and static files dynamically inside templates. Example:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<a href="{{ url_for('about') }}">About</a>
```

**`@app.errorhandler(404)`** — Catches unknown URLs and redirects users to the home page instead of showing a raw error.

---

## Common Errors & Fixes

| Error | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: flask` | Flask not installed | Run `pip3 install flask` |
| `Address already in use` | Port 5000 is taken | Change to `app.run(port=5001)` in `app.py` |
| CSS not loading | Wrong static path | Ensure CSS is in `static/css/` and use `url_for('static', ...)` |
| `TemplateNotFound` | HTML not in `templates/` | Move all `.html` files into the `templates/` folder |
| `brew: command not found` | Homebrew not installed | Install from [brew.sh](https://brew.sh) |

---

## Authors

PulseLife Gym website — built as a Flask routing exercise.
