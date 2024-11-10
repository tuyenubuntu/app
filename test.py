from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('learn.html')


@app.route('/about')
def log():
    return render_template('learn2.html', title='About')

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=8000,debug=True)