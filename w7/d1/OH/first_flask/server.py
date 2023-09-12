from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/say/<string:name>')
def say_name(name):
    return f'Hello my name is {name}'

@app.route('/say/<string:name>/<int:num>')
def num(name, num):
    return render_template('index.html', name=name, num=num)



if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5001)