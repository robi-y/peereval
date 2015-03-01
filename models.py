from google.appengine.ext import ndb

class Evaluation(ndb.Model):
    username = ndb.StringProperty(required=True)
    groupname = ndb.StringProperty(required=True)
    iteration = ndb.IntegerProperty(required=True)
    peer = ndb.StringProperty(required=True)
    grade = ndb.IntegerProperty(required=True)
    justification = ndb.TextProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def remaining_evaluations_query(cls, username, iteration):
        peers = User.peers(username)

        qry = cls.query(username=username, iteration=iteration).order(
            -cls.date_created)
        return qry

class User(ndb.Model):
    username = ndb.StringProperty()
    groupname = ndb.StringProperty()

class Group(ndb.Model):
    groupname = ndb.StringProperty()
    current_iteration = ndb.IntegerProperty()


