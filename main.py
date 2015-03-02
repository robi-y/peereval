#!/usr/bin/env python

import webapp2

from google.appengine.api import users
#see http://stackoverflow.com/a/22275563/4388 for oauth with github

import os
import jinja2

from models import Evaluation, User, Group

from utils import Utils

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class PeerEval(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        _username = 'student1' # query User
        _iteration = 0 #query Group
        if user is not None:
            logout_url = users.create_logout_url(self.request.uri)
            template_context = {
                'user': user.nickname(),
                'logout_url': logout_url,
                'remaining_peers': self.ramaining_peers(_username, _iteration)
            }
            self._render_template(template_context)
        else:
            login_url = users.create_login_url(self.request.uri)
            self.redirect(login_url)

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.error(401)

        _username = 'student1' # query User
        _groupname = 'group1' #query Group
        _iteration = 0 #query Group
        evaluation = Evaluation(username=_username,
                groupname=_groupname,
                iteration=_iteration,
                peer=self.request.get('peer'),
                grade=int(self.request.get('grade')),
                justification=self.request.get('justification'),
                         )
        evaluation.put()

        #qry_remaining_peers = Evaluation.remaining_evaluations_query(_username, _iteration)

        logout_url = users.create_logout_url(self.request.uri)

        template_context = {
            'user': user.nickname(),
            'logout_url': logout_url,
            'eval_peer': self.request.get('peer'),
            'remaining_peers':  self.ramaining_peers(_username, _iteration)
        }
        self._render_template(template_context)
    
    def _render_template(self, context):
        template = jinja_env.get_template('main.html')
        self.response.out.write(
            template.render(context))
        
    def ramaining_peers(self, username, iteration):
        peers = [user.username for user in User.qry_peers(username).fetch()]
        evaluated = [evaluation.peer for evaluation in Evaluation.qry_evaluated_peers(username, iteration).fetch()]
        return Utils.complements(peers, evaluated)

class Populator(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('Welcome, %s!' % user.nickname())
        if users.is_current_user_admin():
#            evaluation = Evaluation(username='student1',
#                groupname='group1',
#                iteration=0,
#                peer='student3',
#                grade=-3,
#                justification='did not contribute'
#            )
#            evaluation.put()
            student = User(username='student1', groupname='group1')
            student.put()
            student = User(username='student2', groupname='group1')
            student.put()
            student = User(username='student3', groupname='group1')
            student.put()
            student = User(username='student4', groupname='group1')
            student.put()
            self.response.out.write('\nDone populating!')
            
app = webapp2.WSGIApplication([
    ('/', PeerEval),
    ('/populate', Populator)
], debug=True)
