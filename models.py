from google.appengine.ext import ndb

class Evaluation(ndb.Model):
    username = ndb.StringProperty()
    groupname = ndb.StringProperty()
    peer = ndb.StringProperty()
    grade = ndb.IntegerProperty()
    justification = ndb.TextProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    username = ndb.StringProperty()
    groupname = ndb.StringProperty()

class Group(ndb.Model):
    groupname = ndb.StringProperty()
    iteration = ndb.IntegerProperty()


