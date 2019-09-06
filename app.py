from flask import Flask, render_template


app = Flask(__name__)

#@app.route('/')
#def hello():
#   return '<h1>Hello WOrld!</h1>'

@app.route('/<name>')
def hello_name(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

