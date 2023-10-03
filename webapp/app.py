from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        return "Hello %s %s " % (fname, lname)
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is about us'
