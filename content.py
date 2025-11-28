# content.py
# All portfolio data will live inside this DATA dict.
# We'll expand this with real Unreal Engine portfolio content next.

DATA = {
    "site": {
        "title": "Your Name | Unreal Engine Developer",
        "description": "Portfolio of an Unreal Engine game developer.",
    },
    "hero": {
        "name": "Your Name",
        "role": "Unreal Engine Developer",
        "tagline": "I build immersive real-time experiences with Unreal Engine.",
        "summary": "Short intro about you. We will customize this later.",
        "primary_cta": {
            "label": "View Projects",
            "href": "#projects",
        },
        "secondary_cta": {
            "label": "Contact Me",
            "href": "#contact",
        },
        "socials": [
            {
                "label": "GitHub",
                "icon": "fa-brands fa-github",
                "href": "https://github.com/yourusername",
            },
        ],
    },
    "about": {
        "title": "About Me",
        "content": [
            "I am an Unreal Engine developer passionate about real-time graphics and gameplay.",
        ],
        "highlights": [
            "Unreal Engine 4 / 5",
            "C++ & Blueprints",
        ],
    },
    "skills": {
        "title": "Skills",
        "groups": [],
    },
    "projects": {
        "title": "Projects",
        "items": [],
    },
    "experience": {
        "title": "Experience",
        "items": [],
    },
    "education": {
        "title": "Education",
        "items": [],
    },
    "contact": {
        "title": "Contact",
        "subtitle": "Let’s build something cool.",
        "email": "you@example.com",
        "location": "Your City",
        "availability": "Open to opportunities.",
        "note": "This is placeholder text; we’ll customize later.",
    },
}
