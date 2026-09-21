from copy import deepcopy
from typing import Any


_NOTES: list[dict[str, Any]] = [


    {

        
    "id":1,
    "title":"Django introduction",
    "body": "Lorem ipsum dolor",
    "tag": "django",
    "category": "backend"


    },

    {
        "id": 2,
        "title": "Django models",
        "body": "Learn how to define database models in Django.",
        "tag": "django",
        "category": "backend",
    },
    {
        "id": 3,
        "title": "Django views",
        "body": "Understanding function-based and class-based views.",
        "tag": "django",
        "category": "backend",
    },
    {
        "id": 4,
        "title": "Django URLs",
        "body": "Learn how URL routing works in Django applications.",
        "tag": "django",
        "category": "backend",
    },
    {
        "id": 5,
        "title": "Django templates",
        "body": "Using Django templates to render dynamic HTML pages.",
        "tag": "django",
        "category": "frontend",
    },
    {
        "id": 6,
        "title": "Django REST Framework",
        "body": "Building REST APIs with Django REST Framework.",
        "tag": "drf",
        "category": "backend",
    },
    {
        "id": 7,
        "title": "Python basics",
        "body": "Variables, functions, loops, and data structures in Python.",
        "tag": "python",
        "category": "programming",
    },
    {
        "id": 8,
        "title": "SQL introduction",
        "body": "Basic SQL queries for working with relational databases.",
        "tag": "sql",
        "category": "database",
    },
    {
        "id": 9,
        "title": "Git basics",
        "body": "Learn commits, branches, merging, and version control.",
        "tag": "git",
        "category": "tools",
    },
    {
        "id": 10,
        "title": "API authentication",
        "body": "Understanding tokens, sessions, and authentication methods.",
        "tag": "api",
        "category": "backend",
    },



]


_next_id = 11



def list_notes() -> list[dict[str, Any]]:

    return deepcopy(_NOTES)



def get_note(note_id: int) -> dict[str, Any]| None:

    for note in _NOTES:
        if note["id"] == note_id:
            return deepcopy(note)
    return None



def create_note (*, title: str, body: str, tag: str, category: str,) -> dict[str, Any]:

    global _next_id
    note = {

        "id": _next_id,
        "title": title.strip(),
        "body": body.strip(),
        "tag": tag.strip(),
        "category":  category.strip(),



    }

    _NOTES.append(note)
    _next_id += 1
    return deepcopy(note)