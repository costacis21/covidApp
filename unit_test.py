from app import uploadForm,reportExposure,models
from sqlalchemy import update
from datetime import datetime

def test_uploadUser(testUser:models.User):
    uploadForm.uploadUser(testUser)
    queryResult = models.User.query.filter_by(name = testUser.name , phone=testUser.phone)
    assert ((queryResult[0].name==testUser.name )& (queryResult[0].phone==testUser.phone)),"uploadForm.uploadUser didn't add user"



def test_reportInfection():
    testUser= models.User(name='Giorgos', phone=101010101,status = "Infected",dateTime=datetime.now())
    uploadForm.reportInfection(testUser)
    queryResult = models.User.query.filter_by(name = testUser.name , phone=testUser.phone)
    assert ((queryResult[0].status=="Infected")&\
            (queryResult[0].name==testUser.name )&\
            (queryResult[0].phone==testUser.phone))\
            ,"uploadForm.reportInfection didn't change user's status to infected"


testUser= models.User(name='Giorgos', phone=101010101)
test_uploadUser(testUser)

newTestUser= models.User(name='Sam', phone=80808080)
test_uploadUser(newTestUser)

test_reportInfection()




    
