from flask import Flask, request, render_template, redirect, flash
#from flask_wtf import form, StringField
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

# shouldn't need two routes to the same location
# just check what brought you here
'''
@app.route("/", methods=['POST'])
def get_username():
    username = cgi.escape(request.form['username'])
    if (len(username)<3) or (len(username)>20):
        error = "Sorry, but that's not a valid username"
        return error    

@app.route("/", methods=['POST'])
def get_password():  
    password = cgi.escape(request.form['password'])
    if (len(password)<3) or (len(password)>20):
        error = "Sorry, but that's not a valid password"
        return error   
        
@app.route("/", methods=['POST'])
def confirm_password():
    verify = cgi.escape(request.form['verify'])
    if verify != password: 
        error = "Oops, your passwords don't match!"
        return error
'''

# Create a form to regiter with
'''
class RegisterForm(Form):
    username = StringField('username')
'''


@app.route("/", methods=['GET','POST'])
def forms():
    
    if request.method == 'POST':
        username = cgi.escape(request.form['username'])
        password = cgi.escape(request.form['password'])
        verify = cgi.escape(request.form['verify'])
        email = cgi.escape(request.form['email'])
        if username == '':
            render_template('welcome.html')
        #handle post validate fields
        redirect('welcome')
    # first time getting the page render it for them
    elif request.method == 'GET':
        render_template('welcome.html')


    
    return render_template('forms.html')
 
@app.route("/welcome", methods=['POST'])
def welcome():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    verify = cgi.escape(request.form['verify'])
    email = cgi.escape(request.form['email'])
    if ((len(username)>3) and (len(username)<20)) and (((len(password)>3) and (len(password)<20))) and (verify == password) and (' ' not in email) and ('@' in email) and ('.' in email):
        return render_template('welcome.html', username=username)

'''     
@app.route("/")
def index():
    user_error = request.args.get("error")
    return render_template('forms.html', error=user_error and cgi.escape(user_error, quote=True))
'''

def email_check(email):
    if ' ' in email: 
        error = "Sorry, but that's not a valid email address"
        return error    
    if '@' not in email: 
        error = "Sorry, but that's not a valid email address"
        return error      
    if '.' not in email: 
        error = "Sorry, but that's not a valid email address"
        return error

app.run()



