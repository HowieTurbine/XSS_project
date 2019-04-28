from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/demo1', methods=['GET', 'POST'])
def demo1():
    return render_template('input.html')


@app.route('/demo2', methods=['GET', 'POST'])
def demo2():
    return render_template('login.html')


@app.route('/demo2_2', methods=['GET', 'POST'])
def demo2_2():
    return render_template('fake_website.html')


@app.route('/save', methods=['GET', 'POST'])
def save_cookie():
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')

        print(email)
        print(password)
        print(remember)

        if remember == 'on':
            # Response with cookie
            response = make_response('OK with cookie')
            response.set_cookie('email', email)
            response.set_cookie('password', password)
            return response
        else:
            # Response without cookie
            response = make_response('OK with out cookie')
            response.delete_cookie('email')
            response.delete_cookie('password')
            return response


if __name__ == '__main__':
    app.run()
