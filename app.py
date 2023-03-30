from flask import Flask, render_template
from application import app 
app = Flask(__name__)

@app.route('/')
def add_book():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
