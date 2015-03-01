#!/usr/bin/env python

import webapp2

from google.appengine.api import users
#see http://stackoverflow.com/a/22275563/4388 for oauth with github

import os
import jinja2

from models import Evaluation

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user is not None:
            logout_url = users.create_logout_url(self.request.uri)
            template_context = {
                'user': user.nickname(),
                'logout_url': logout_url,
            }
            template = jinja_env.get_template('main.html')
            self.response.out.write(
                template.render(template_context))
        else:
            login_url = users.create_login_url(self.request.uri)
            self.redirect(login_url)

    def post(self):
        user = users.get_current_user()
        if user is None:
            self.error(401)

        _username = 'jce.student' # query User
        _groupname = 'BestBuy' #query Group
        evaluation = Evaluation(username=_username,
                groupname=_groupname,
                peer=self.request.get('peer'),
                grade=int(self.request.get('grade')),
                justification=self.request.get('justification'),
                         )
        evaluation.put()

        logout_url = users.create_logout_url(self.request.uri)
        template_context = {
            'user': user.nickname(),
            'logout_url': logout_url,
            'eval_peer': self.request.get('peer'),
        }
        template = jinja_env.get_template('main.html')
        self.response.out.write(
            template.render(template_context))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
