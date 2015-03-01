#!/usr/bin/env python

import webapp2

from google.appengine.api import users
#see http://stackoverflow.com/a/22275563/4388 for oauth with github

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user is not None:
            self.response.write('Hello PeerEval!')
        else:
            login_url = users.create_login_url(self.request.uri)
            self.redirect(login_url)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
