# 🔖 Personal Portfolio Website

A medium-level personal portfolio website built with Python and Flask. This project showcases a simple but functional portfolio to present your skills, projects, and contact information.

---

## ✅ Features

- Homepage with introduction and summary
- Projects page to display your work
- Contact page with a working contact form using Flask-WTF
- Modular Flask app structure
- SQLite database integration (optional for future expansions)
- Basic styling with CSS (can be extended with Bootstrap or other frameworks)

---

## ✅ Technologies Used

- Python 3.x
- Flask
- Flask-WTF (for form handling and validation)
- Flask-SQLAlchemy (optional, for database integration)
- HTML5 & CSS3
- Jinja2 templating engine

---

## ✅ Project Structure
```text
portfolio/
 │
 ├── app/
 │ ├── init.py # Flask app factory and setup
 │ ├── routes.py # Route definitions
 │ ├── models.py # Database models (optional)
 │ ├── forms.py # WTForms form definitions
 │ ├── templates/ # HTML templates
 │ │ ├── base.html
 │ │ ├── index.html
 │ │ ├── projects.html
 │ │ └── contact.html
 │ └── static/ # Static files: CSS, JS, images
 │
 ├── config.py # Configuration file
 ├── run.py # Application entry point
 └── requirements.txt # Python dependencies
```

## ✅ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

## ✅ Install dependencies

```bash
pip install -r requirements.txt
```

## ✅ Run the application

```bash
python run.py
```


### Open your browser and visit

```cpp
http://127.0.0.1:5000
```