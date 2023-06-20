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


# practising redirect to another page
@app.route('/home/login')
def send_login_page():
    return render_template('login.html')


@app.route('/home/login_success', methods=['POST'])
def login():
    # request.form is a dictionary, 'username' is a key, which is corresponding to the name attribute
    username = request.form['username']
    password = request.form['password']
    return render_template('login_success.html', username=username, password=password)


# 如何在flask application中接收該html回傳的username和password
if __name__ == "__main__":
    app.run(debug=True)
