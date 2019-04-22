from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/demo1',methods=['GET','POST'])
def demo1():
    return render_template('input.html')


@app.route('/demo3',methods=['GET','POST'])
def demo3():
    return render_template('login.html')


@app.route('/list',methods=['GET','POST'])
def list_word():
    if request.method == 'POST':
        data = request.get_data()

        print(data)
        return data


if __name__ == '__main__':
    app.run()
