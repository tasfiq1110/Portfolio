import os
from datetime import datetime

from flask import Flask, render_template, request
from content import DATA

app = Flask(__name__)

# Path where messages will be stored
MESSAGE_DIR = os.path.join(app.root_path, "messages")
os.makedirs(MESSAGE_DIR, exist_ok=True)
MESSAGE_FILE = os.path.join(MESSAGE_DIR, "contact_messages.log")


@app.route("/")
def index():
    return render_template("index.html", data=DATA)


def append_message_to_file(name: str, email: str, message: str) -> None:
    """Append a single contact message as a line of text."""
    timestamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    line = (
        f"[{timestamp}]\n"
        f"Name   : {name}\n"
        f"Email  : {email}\n"
        f"Message: {message}\n"
        f"{'-'*40}\n"
    )
    with open(MESSAGE_FILE, "a", encoding="utf-8") as f:
        f.write(line)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    # Save it to the file on your web host
    append_message_to_file(name, email, message)

    # Re-render page with success flag
    return render_template("index.html", data=DATA, contact_success=True)


# OPTIONAL: simple viewer page for yourself
@app.route("/messages")
def view_messages():
    """Very basic viewer for stored messages.

    ⚠ If your site is public, consider changing the route path
    to something less guessable, or protect it behind auth later.
    """
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "No messages yet."

    # Render as plain text in browser
    return f"<pre>{content}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
