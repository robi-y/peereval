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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        _iteration = 0 #query Group
        if user is not None:
            logout_url = users.create_logout_url(self.request.uri)
            template_context = {
                'user': user.nickname(),
                'logout_url': logout_url,
                'remaining_peers': self.ramaining_peers(user, _iteration)
            }
            self._render_template(template_context)
        else:
            login_url = users.create_login_url(self.request.uri)
            self.redirect(login_url)

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.error(401)

        _username = 'jce.student' # query User
        _groupname = 'BestBuy' #query Group
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
            'remaining_peers':  self.ramaining_peers(user, _iteration)
        }
        self._render_template(template_context)
    
    def _render_template(self, context):
        template = jinja_env.get_template('main.html')
        self.response.out.write(
            template.render(context))
        
    def ramaining_peers(self, user, iteration):
        peers = User.qry_peers(user) #.fetch()
        evaluated = Evaluation.qry_evaluated_peers(user, iteration) #.fetch()
        return Utils.complements(peers, evaluated)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
