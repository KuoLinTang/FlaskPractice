from flask import Flask, render_template, request

# templage for HTML, static for images
app = Flask(__name__, static_folder='./static', template_folder='./template')


@app.route('/')
def root():
    return "This is the root."


@app.route('/home/')
def home():
    return render_template('homepage.html')


# testing passing parameters using URL string
@app.route('/home/get_request_params/<username>/')
def print_username(username):
    return f'USERNAME: {username}'


# testing passing parameters using arguments
@app.route('/home/get_request_params/')
def request_username():
    username = request.args.get("username")
    password = request.args.get("password")
    return f'USERNAME: {username} AND PASSWORD: {password}'


# practicing passing parameters to a template
@app.route('/home/pass_args_to_html/')
def testing_html_parameter():
    name = request.args.get('name')
    username = request.args.get("username")
    return render_template('page_with_parameter.html', name=name, username=username)


if __name__ == "__main__":
    app.run(debug=True)
