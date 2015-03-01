from google.appengine.ext import ndb

class Evaluation(ndb.Model):
    username = ndb.StringProperty(required=True)
    groupname = ndb.StringProperty(required=True)
    peer = ndb.StringProperty(required=True)
    grade = ndb.IntegerProperty(required=True)
    justification = ndb.TextProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    username = ndb.StringProperty()
    groupname = ndb.StringProperty()

class Group(ndb.Model):
    groupname = ndb.StringProperty()
    iteration = ndb.IntegerProperty()


