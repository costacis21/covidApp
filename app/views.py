from flask import flash, render_template, redirect, url_for
from app import app
from .forms import userForm
from app import models
from app import uploadForm


@app.route('/', methods=['GET','POST'])
def index():

    form = userForm()

    # if form is submited without validation errors
    if form.validate_on_submit():
        newUser = models.User(name=form.name.data, phone=form.phone.data, status = "clean") #create new user with the form data
        uploadForm.uploadUser(newUser)        
        return redirect(url_for('index')) #refresh in order to update info on table


    return render_template('index.html',
                           title='Add users',
                           form=form
                        )


@app.route('/reportInfection', methods=['GET','POST'])
def reportInfection():

    form = userForm()
    error=None
    
    # if form is submited without validation errors   
    if form.validate_on_submit():
        
        infectedUser = models.User(name=form.name.data, phone=form.phone.data) #create new user with the form data
    
        if(uploadForm.reportInfection(infectedUser)==0): #report the infection if user is valid
            error="no such user"
        else:
            return redirect(url_for('reportInfection')) #refresh in order to have empty form


    return render_template('reportInfection.html',
                        title='Report Infection',
                        form=form,
                        message=error)



"""
FOR ADMIN AND DEBUG PURPOSES ONLY
"""
@app.route('/allUsers', methods=['GET','POST'])
def allUsers():
    

    return render_template('allUsers.html',
                           title='AllUsers',
                           users=uploadForm.allUsers()
                        )



