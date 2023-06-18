from flask import Flask, render_template, request

# templage for HTML, static for images
app = Flask(__name__, static_folder='./static', template_folder='./template')


@app.route('/')
def root():
    return "This is the root."


@app.route('/home')
def home():
    return render_template('homepage.html')


# testing passing parameters using URL string
@app.route('/home/test/<username>')
def print_username(username):
    return username


# testing passing parameters using arguments
@app.route('/home/test/')
def request_username():
    username = request.args.get("username")
    return username


if __name__ == "__main__":
    app.run(debug=True)
