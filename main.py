from flask import Flask, request, render_template
import cgi

app = Flask(__name__)

error_code = False

app.config['DEBUG'] = True 


@app.route("/", methods=['GET','POST'])
def forms():
    error_code = False
    
    if request.method == 'GET':
        return render_template('forms.html', error_code=error_code)

    elif request.method == 'POST':

        username = cgi.escape(request.form['username'])
        password = cgi.escape(request.form['password'])
        verify = cgi.escape(request.form['verify'])
        email = cgi.escape(request.form['email'])
       
        # Validate usernames length
        user_error = ''
        if not ((len(username)>3) and (len(username)<20)):
            error_code = True
            user_error = "Your username needs to be between 3 and 20 characters"
            
        # Validate passwords length
        password_error = ''
        if not (((len(password)>3) and (len(password)<20))):
            error_code = True
            password_error = "Passwords need to be between 3 and 20 characters"

        verify_error = ''
        if verify == '':
            error_code = True
            verify_error = "Passwords need to be between 3 and 20 characters"
        # Validate passwords match
        if verify != password:
            error_code = True
            verify_error = "Passwords didn't match"

        # check for @ symbol and dot in string or for white space
        email_error = ''
        if email == '':
            email_error = ''
        elif '@' not in email and '.' not in email or ' ' in email:
                error_code = True
                email_error = "Not a valid email address"
            
        # render the page again with errors if error_code is True
        if error_code == True:
            return render_template('forms.html', username=username, email=email, error_code=error_code, user_error=user_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
        else:
            return render_template('welcome.html', username=username)
    
    return render_template('forms.html', error_code=error_code)
 




app.run()