import json
class User:
    def __init__(self, fName, lName, email, password, phoneNumber, logged):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.logged =  logged
class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"fName": obj.fName, "lName": obj.lName, "email": obj.email, "password": obj.password, "phoneNumber": obj.phoneNumber, "logged":obj.logged}
        return super().default(obj)

class Projec:
    def __init__(self, title, details, totalTarget, reachedTarget, startDate, endDate, ownerEmail):
        self.title = title
        self.details = details
        self.totalTarget = totalTarget
        self.reachedTarget = reachedTarget
        self.startDate = startDate
        self.endDate = endDate
        self.ownerEmail = ownerEmail

class ProjEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Projec):
            return {"title": obj.title, "details": obj.details, "totalTarget": obj.totalTarget, "reachedTarget": obj.reachedTarget, "startDate": obj.startDate, "endDate":obj.endDate, "ownerEmail":obj.ownerEmail}
        return super().default(obj)
