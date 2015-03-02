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
    def qry_evaluated_peers(cls, username, iteration):
        qry = cls.query().filter(ndb.AND(cls.username==username, cls.iteration==iteration)).order(-cls.date_created)
        return qry #['student2','student4']

class User(ndb.Model):
    username = ndb.StringProperty()
    groupname = ndb.StringProperty()
    
    @classmethod
    def qry_peers(cls, user):
        usergroup = 'group1'
        peers = cls.query().filter(cls.groupname==usergroup)
        return peers #['student1', 'student2', 'student3', 'student4']

class Group(ndb.Model):
    groupname = ndb.StringProperty()
    current_iteration = ndb.IntegerProperty()


