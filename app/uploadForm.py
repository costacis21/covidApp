from app import db,models
from datetime import datetime
from sqlalchemy import update
from app import reportExposure,reportExposure

def uploadUser(user: models.User):
    # add user to db
    user.dateTime=datetime.now()
    db.session.add(user)
    db.session.commit()


def reportInfection(user: models.User):

    # search for user by phone
    t = models.User.query.filter_by(phone=user.phone).all()

    #if user exists with the same name and number, change its status to infected
    if(len(t)>0):
        if((t[0].name==user.name)):
            print("user {} found changing status to infected".format(t[0].name))
            t[0].status="Infected"
            db.session.commit()
            reportExposure.notifyUsers(t[0])
            return 1
        else:
            print("user not found found")
            return 0
    return 0

    
    

def allUsers():
    # used to monitor db
    users=models.User.query.all()
    return users
