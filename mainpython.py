import Models as dbHandler
import codecs
from flask import Flask,render_template,request
import sqlite3
import cart as dbHandler2


auth = False
# createing objest for flask
app=Flask(__name__)

# @app.route('/mani')
# def contact():
#     f = codecs.open('C:/Users/Manikanta D K/python ml/task to srore data/templates/contact.html', 'r')
#     return f.read()
    # return "SUCCESS"
    # return render_template('contact.html')

# @app.route('/contact2')  
# def contact():
#     return render_template('contact2.html')

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        # username = request.form["username"]
        # password = request.form["password"]
        # dbHandler.insertUser(username,password)
        # users = dbHandler.retriveUsers()
        return "Sucess"
    else:
        return render_template("contactt.html")
    
@app.route('/signUpSubmit',methods=['POST','GET'])
def signUp():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        confirmPassword = request.form["confirmPassword"]
        if password != confirmPassword:
            return "password and confirm assword must match"
        dbHandler.insertUser(username,password)
        # users = dbHandler.retriveUsers()
        return username
    else:
        return render_template("contact.html")
    return "404 NOT found"

@app.route('/loginSubmit',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        # dbHandler.insertUser(username,password)
        users = dbHandler.retriveUsers()
        #data = cur.fetchall()
        for i,j in users:
            if i == username and j == password:
                auth = True
            else:
                pass

        if auth == True:
            return render_template("application.html")
        
        else:
           return "wrong username or password"
        return 
    return "404 NOT found"
@app.route('/loginSubmit',methods=['POST','GET'])
def application():
    return render_template("application.html")

    
@app.route('/cart', methods=['POST', 'GET'])
def abc():
    if request.method=='POST':
        cart_items ="samsung"
        # username = request.form["username"]
        # password = request.form["password"]
        dbHandler2.insertUser(cart_items)
        # users = dbHandler.retriveUsers()
        return render_template("aa.html")
    
@app.route('/cart1', methods=['POST', 'GET'])
def abcv():
    if request.method=='POST':
        cart_items ="nokia"
        # username = request.form["username"]
        # password = request.form["password"]
        dbHandler2.insertUser(cart_items)
        # users = dbHandler.retriveUsers()
        return render_template("aa.html")
    
@app.route('/cart2', methods=['POST', 'GET'])
def abcd():
    if request.method=='POST':
        cart_items ="mi"
        # username = request.form["username"]
        # password = request.form["password"]
        dbHandler2.insertUser(cart_items)
        # users = dbHandler.retriveUsers()
        return render_template("aa.html")
    
@app.route('/car', methods=['POST', 'GET'])
def abcde():
    if request.method=='POST':
        result = dbHandler2.retriveUsers()
      
        return render_template("man.html",result=result)
    else:
        return "i have got data"

@app.route('/mm', methods=['POST', 'GET'])
def abcdef():
    return render_template("cart_check.html")
@app.route('/manusj', methods=['POST', 'GET'])
def abcdefs():
    return render_template("submit.html")
@app.route('/manuj', methods=['POST', 'GET'])
def abcdesfs():
    return render_template("store.html")
    
        
if __name__=='__main__':
    app.run(debug=True) 

    

