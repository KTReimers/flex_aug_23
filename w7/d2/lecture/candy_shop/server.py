from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key="shhhh my secret"

@app.route('/')
def index():
    return render_template("register.html")

@app.route('/user/register', methods=['POST'])
def register_user():
    print(request.form)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    return redirect('/order')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/order/process', methods=['POST'])
def process_order():
    session['snickers'] = request.form['snickers']
    session['milkyway'] = request.form['milkyway']
    session['butterfinger'] = request.form['butterfinger']
    session['hersheys_almond'] = request.form['hersheys_almond']
    session['total'] = int(request.form['snickers']) + int(request.form['milkyway']) + int(request.form['butterfinger']) + int(request.form['hersheys_almond'])
    return redirect('/receipt')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

if __name__ == "__main__":
    app.run(debug=True)# mac users add port=5001, host="localhost"
