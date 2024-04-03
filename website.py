from flask import Flask, render_template, request
from threading import Thread
from process import attention

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index2.html')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/validate',  methods=['POST'])
def success():

	t3 = Thread(target = attention)
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']
		if email == 'ayush@gmail.com' and password == '1234':
			t3.start()
			return render_template('index2.html', email=email)
		else:
			return render_template('index.html')

if __name__ == '__main__':
    app.run()