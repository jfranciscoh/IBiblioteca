from flask import Flask, render_template

app = Flask(__name__)

@app.route('/addbook')
def add_book():
    return render_template('addbook.html')

if __name__ == '__main__':
    app.run(debug=True)
