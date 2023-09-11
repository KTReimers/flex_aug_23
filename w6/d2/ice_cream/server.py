from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ice_cream')
def ice_cream_flavors():
    ice_cream=[
        {"name":"cookies n cream", "favorited": "Will"},
        {"name":"Rocky Road", "favorited": "Jane"},
        {"name":"Strawberry", "favorited": "Kyle"},
        {"name":"Strawberry", "favorited": "Kyle"},
        {"name":"Strawberry", "favorited": "Kyle"},
        {"name":"Strawberry", "favorited": "Kyle"}
    ]
    return render_template('ice_cream.html',flavors=ice_cream)

# @app.route('/newPage')
# def new(flavors):
#     return f'{flavors}'











if __name__ == "__main__":
    app.run(debug=True, port=5001)
