from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="shhhhhh"

@app.route('/')
def home():
    if 'Chocolate' not in session:
        session['Chocolate'] = 0
    if 'Vanilla' not in session:
        session['Vanilla'] = 0
    if 'Strawberry' not in session:
        session['Strawberry'] = 0

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

@app.route('/add', methods=['POST'])
def add():
    print(request.form)
    # request.form['first_name']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['flavor'] = request.form['flavor']
    if(request.form['flavor'] == "Chocolate"):
        session['Chocolate'] += 1
    elif(request.form['flavor'] == "Vanilla"):
        session['Vanilla'] +=1
    else:
        session['Strawberry'] += 1
    return redirect('/ice_cream')











if __name__ == "__main__":
    app.run(debug=True, port=5001)
