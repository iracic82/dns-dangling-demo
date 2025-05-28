from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MyCorp Portal</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- External JS loaded from hijackable CNAME target -->
        <script src="http://cdn.mycorp.internal/marketing.js"></script>
    </head>
    <body class="bg-light text-center">
        <div class="container py-5">
            <h1 class="display-4 mb-4">🚪 Welcome to MyCorp Portal</h1>
            <p class="lead">This is a simulation of a DNS dangling vulnerability affecting external JS assets.</p>
            <hr class="my-4">
            <p>External script is loaded from <code>cdn.mycorp.internal</code>.</p>
            <div id="script-output" class="mt-4"></div>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
