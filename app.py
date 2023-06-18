from flask import Flask, render_template, request

# templage for HTML, static for images
app = Flask(__name__, static_folder='./static', template_folder='./template')


@app.route('/')
def root():
    return "This is the root."


@app.route('/home')
def home():
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(debug=True)
