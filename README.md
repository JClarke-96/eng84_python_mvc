# MVC with Flask
- Install Flask with `pip install flask`
- Create file called app.py
- Import Flask and create app as object of Flask
- Create pages with `@app.route("/name/")`
- Open webpage with `flask run`

## Inheritence with Flask
- Parent file has `{% block head %}{% endblock %}` or `{% block content %}{% endblock%}`
- Block is used to overwrite HTML within the block
- Child uses `{% extends "parent.html" %}` with the same `{% block head %}{% endblock %}`
- This is used to add to the parent HTML file
- When child.html is used, it is added to parent and both are shown