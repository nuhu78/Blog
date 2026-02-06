# Django Blog (myblog)

A simple Django blog project for learning and demonstration.

## Features
- Create, view, and list blog posts
- User signup, login, and profile
- Simple templates provided in `templates/`

## Tech
- Python 3.x
- Django (project created with `manage.py`)

## Quick setup

1. Clone or copy the repo to your machine.
2. Create and activate a virtual environment.

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# or cmd
.\venv\Scripts\activate
```

3. Install dependencies (if you have a `requirements.txt` add it, otherwise install Django):

```bash
pip install django
# or
pip install -r requirements.txt
```

4. Apply migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ to view the site.

## Project structure
- `manage.py` — Django management script
- `db.sqlite3` — default SQLite database
- `blog/` — app with models, views, forms, templates
- `myblog/` — project settings and URL config
- `templates/` — base and app templates (`blog/`, `user/`)

## Templates
Templates live under `templates/`:
- `templates/base.html`
- `templates/blog/post_list.html`, `post_detail.html`, `post_create.html`
- `templates/user/login.html`, `signup.html`, `profile.html`

## Tests
Run tests with:

```bash
python manage.py test
```

## Contributing
Suggestions and improvements welcome — open an issue or submit a PR.

## License
Add a LICENSE file if you want to specify a license for this project.

---
If you want, I can customize this README with deployment steps, a `requirements.txt`, or CI instructions.
