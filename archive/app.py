from flask import Flask, render_template_string
import markdown
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read the Markdown file
    with open('index.md', 'r') as file:
        md_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Define a basic HTML template
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Moorissa Tjokro</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="container-lg px-3 my-5 markdown-body">
            {{ content|safe }}
        </div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
        <script>anchors.add();</script>
    </body>
    </html>
    """

    # Render the HTML template with Markdown content
    return render_template_string(template, content=html_content)

if __name__ == '__main__':
    app.run(debug=True)