# Discography 

A fan-made Django web application for cataloguing a band's discography: albums, songs and the members credited on each track. It is built around Stray Kids as the example subject, but nothing is hard-coded, so every album, song and member is created through the web interface.


Built as the individual project for the SoftUni **Django Basics** course (retake exam).

---

## Features

- **Albums**: full CRUD (create, list, detail, edit, delete with a confirmation page), sorting by newest, oldest or title, and a track count and total running time per album.
- **Songs**: full CRUD with a delete confirmation, search by title (at least 2 characters), filtering by album and by credited member, and several sort orders.
- **Members**: create, list, detail and edit, with a credits list showing every song a member is credited on.
- **Songs without an album**: a song can exist as a standalone release. Deleting an album keeps its songs and turns them into standalone songs.
- **Validation** in both forms and models, with friendly custom error messages, labels, help texts and placeholders.
- **Custom template filter and tag** (`duration` and `album_total_duration`), plus built-in filters such as `date`, `pluralize`, `truncatewords` and `default`.
- **Custom 404 page**, a shared base template, reusable partials (navbar, footer, album card) and a Bootstrap 5 layout.
- Works from an **empty database**: no fixtures, no prepopulated data, no admin panel needed.

---

## Tech stack

- Python and Django 6.1
- SQLite
- Bootstrap 5.3 (loaded from a CDN, so an internet connection is needed to see the styling)
- Django Template Engine

Authentication and user management are intentionally not implemented, as the project requirements exclude them.

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Rawi-wi/django_project_discography
cd django_project_discography
```

### 2. Create and activate a virtual environment

**Windows (PowerShell or Command Prompt)**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply the database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

### Environment variables

None are required. The project runs with its default configuration, uses a local SQLite database file (`db.sqlite3`, created by `migrate`) and needs no credentials. The development `SECRET_KEY` in `config/settings.py` is for local use only and should be replaced and moved to an environment variable before any real deployment.

---

## How to try it out

The database starts empty, so create things in this order using only the navigation bar:

1. **Members**: click *Members*, then *Add member*, and create one or more members.
2. **Albums**: click *Albums*, then *Add album*.
3. **Songs**: click *Songs*, then *Add song*. Pick an album (or leave it empty for a standalone song) and tick the credited members.
4. Open any detail page to see the links between albums, songs and members.

---

## Project structure

```
django_project_discography/
├── config/                 # Project settings, root URLs and the home page view
├── albums/                 # Album model, forms, views, validators, templates
├── songs/                  # Song model, forms, views, validators, templates
│   └── templatetags/       # Custom template filter and tag
├── members/                # Member model, forms, views, validators, templates
├── templates/              # base.html, home.html, 404.html and partials/
├── manage.py
└── requirements.txt
```

### Apps and their responsibilities

| App | Responsibility |
|---|---|
| `albums` | Albums (title, type, release date, cover link) and their pages |
| `songs` | Songs, the credits link to members, filtering and sorting, custom template tags |
| `members` | Band members and their profile and credits pages |

---

### Models

**Album**

| Field | Notes |
|---|---|
| `title` | Text, at least 2 characters |
| `release_date` | Date, cannot be in the future |
| `album_type` | Choice: mini album, full album, single or repackage |
| `cover_url` | Optional link, must point to an image file (`.jpg`, `.jpeg`, `.png`, `.webp` or `.gif`) |
| `description` | Optional text |

Ordered by release date, newest first.

**Member**

| Field | Notes |
|---|---|
| `stage_name` | Unique, cannot consist only of digits or spaces |
| `birth_name` | Text |
| `position` | Optional text |
| `birthday` | Date, cannot be in the future |
| `image_url` | Optional link |
| `bio` | Optional text |

Ordered by stage name.

**Song**

| Field | Notes |
|---|---|
| `title` | Text |
| `album` | Optional foreign key to Album |
| `track_number` | Whole number from 1 to 100 |
| `length_in_seconds` | Whole number from 1 to 1200, displayed as `m:ss` |
| `credited_members` | Many-to-many relationship to Member, optional |
| `description` | Optional text |

A database constraint keeps the pair (`album`, `track_number`) unique, so two songs cannot share a track slot on the same album.

### Relationships

- **Song to Album**: many-to-one (`related_name='songs'`). The relationship uses `SET_NULL`, so deleting an album does not delete its songs.
- **Song to Member**: many-to-many (`related_name='songs'` on Member), used for credits.

---

## Pages and URLs

| URL | Page |
|---|---|
| `/` | Home page |
| `/albums/` | All albums, with sorting |
| `/albums/create/` | Add an album |
| `/albums/<id>/` | Album details, tracklist and running time |
| `/albums/<id>/edit/` | Edit an album |
| `/albums/<id>/delete/` | Delete confirmation |
| `/songs/` | All songs, with search, filters and sorting |
| `/songs/create/` | Add a song |
| `/songs/<id>/` | Song details and credits |
| `/songs/<id>/edit/` | Edit a song |
| `/songs/<id>/delete/` | Delete confirmation |
| `/members/` | All members |
| `/members/create/` | Add a member |
| `/members/<id>/` | Member profile and credits |
| `/members/<id>/edit/` | Edit a member |

Every page is reachable from the navigation bar or from links on other pages, and every page shows the shared footer.

---

## Forms and validation

| Form | Highlights |
|---|---|
| `AlbumForm` | Custom labels, help texts and placeholders. Validators for title length, no future release date and image-type cover links. Custom error messages |
| `SongForm` | Validators for song length and track number. Checks that the track number is unique on the chosen album. The **album field is read-only when editing** a song. Checkbox widget for credited members |
| `MemberForm` | Unique stage name, no future birthday, a stage name that is not only digits. Custom error messages |
| `SongFilterForm` | GET form for searching and filtering songs. The search text must be 2 to 100 characters, and the album, member and sort choices are validated with custom error messages |

Validators live in `validators.py` inside each app.

---

## Custom template tools

Defined in `songs/templatetags/song_extras.py` and loaded with `{% load song_extras %}`:

- `duration` (filter): turns a number of seconds into `m:ss`, for example `185` becomes `3:05`.
- `album_total_duration` (tag): returns the total running time of an album.

---

## Notes and limitations

- Cover and member images are stored as links, not uploaded files.
- Members can be created and edited but not deleted.
- The custom 404 page appears when `DEBUG = False`. With `DEBUG = True`, Django shows its own debug page.
- The `/admin/` route exists by default, but the admin panel is not needed to use the application.

---

## Author

Ralitsa Grudkova
Created as a SoftUni Django Basics project, November 2026.
