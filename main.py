from flask import Flask,render_template

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/lt')
def lt():
    return  'lt'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)