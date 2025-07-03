Flask Learning Project
This repository documents my journey in learning Flask, a lightweight and powerful Python web framework. Throughout this project, I explored essential Flask features, including handling HTTP methods, dynamic URL routing, Jinja templating, and page redirection.

🚀 Features Implemented
1. Handling GET and POST Requests
Implemented routes that respond to both GET and POST HTTP methods. For instance, a login form that displays on a GET request and processes user credentials on a POST request.

2. Dynamic URL Routing with Variable Rules
Utilized Flask's variable rules to create dynamic URLs that capture parts of the URL as variables. For example:
sitepoint.com

python
Copy
Edit
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
This route captures the username from the URL and passes it to the view function. 
sitepoint.com

3. Jinja2 Templating
Leveraged Jinja2, Flask's default templating engine, to render dynamic HTML pages. This includes:
medium.com

Injecting variables into templates.

Using control structures like loops and conditionals.

Template inheritance for maintaining consistent layouts.
medium.com

Example:

html
Copy
Edit
<!-- base.html -->
<!doctype html>
<html>
  <head><title>{% block title %}{% endblock %}</title></head>
  <body>
    {% block content %}{% endblock %}
  </body>
</html>

<!-- index.html -->
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome, {{ username }}!</h1>
{% endblock %}
4. Redirecting to Another HTML Page
Implemented redirection using Flask's redirect() and url_for() functions to navigate users between pages after certain actions, such as form submissions.

Example:

python
Copy
Edit
from flask import redirect, url_for

@app.route('/submit', methods=['POST'])
def submit():
    # Process form data
    return redirect(url_for('thank_you'))
📂 Project Structure
csharp
Copy
Edit
flask_learning_project/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── thank_you.html
└── static/
    └── style.css
🛠️ Technologies Used
Python 3.x

Flask

Jinja2

HTML/CSS

📖 References
Flask Documentation

GeeksforGeeks: Redirecting to URL in Flask

SitePoint: Understanding URL Routing in Flask
flask.palletsprojects.com
geeksforgeeks.org
+1
geeksforgeeks.org
+1
sitepoint.com

