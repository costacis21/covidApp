import sqlalchemy
from datetime import datetime  
from datetime import timedelta  
from app import db,models
import os
from twilio.rest import Client



def notifyUsers(user: models.User):
    #search for users that inputed their info within 3 hours of the infected user.
    l_interval=user.dateTime
    h_interval=l_interval+timedelta(hours=3)
    print(h_interval)
    users= models.User.query.filter(models.User.dateTime <= h_interval).all()   
    print(len(users))
    #send SMS to each user
    for cUser in users:
        if((cUser.phone==user.phone) | (cUser.status=="Infected")):
            continue
        print('sending sms to {}'.format(cUser.phone))
        cUser.status="Exposed"
        sendSMS(cUser)

    
    db.session.commit() 

def sendSMS(user: models.User):
    try:
        #twillo credentials
        account_sid="ACff074262aa261ac1ac62aa0849382b09"
        auth_token = "9d7a3e5252f90d197f8f67bf7040b212"

        client = Client(account_sid,auth_token)

        #create and send message
        message = client.messages.create(
                from_='+13614705055',
                body="You have been exposed to an infected person, please isolate or have a test",
                to=str(user.phone)
                )
    except:
        print("error sending SMS to {}".format(user.phone))

