import json


def make_hashtags():
    """Asks user to input travel locations and creates usable Instagram hashtags."""
    tags = []
    print("Type 'done' when you've added all locations.")
    while True:
        tag = input("Where did you go? -> ")
        if tag.lower() == 'done':
            print("Your blog is ready! Check 'index.html' in your browser.")
            break
        else:
            tags.append(tag)
    return [{"title": t, "tag": t.replace(' ', '').lower()} for t in tags]

try:
    # Read user-provided blog input
    with open('logs.json', 'r') as fin:
        logs = json.load(fin)
except FileNotFoundError:
    # If a user doesn't provide a JSON file, I assume they want it even easier... You're welcome! :)
    logs = make_hashtags()

title = '📷 Lazy'
body = []
for log in logs:
    post = f"""
<section>
    <hr>
    <div class="row align-items-center">
        <div class="col-md-10">
            <h2 class="display-4">{log.get('title', 'Untitled')}</h2>
        </div>
        <div class="col-md-2">
            <footer class="blockquote-footer">{log.get('date', 'sometime before today')}</footer>
        </div>
    </div>
    <div class="row">
        <div class="col-md-2">
            <a href="https://www.instagram.com/explore/tags/{log.get('tag', 'kitten')}" class="btn btn-outline-dark" target="_blank">Check others' pics</a>
        </div>
        <div class="col-md-10">
            <p class="lead">{log.get('text', 'pics say more than words :)')}</p>
        </div>
    </div>
<section>
"""
    body.append(post)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>{title}</title>
</head>
<body>
    <div class="container">
    <h1 class="display-1">📷 Lazy Travel Blog</h1>
"""

for post in body:
    html += post

end = """
    </div>
</body>
</html>"""

html += end

with open('index.html', 'w') as f:
    f.write(html)
