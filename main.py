#!/usr/bin/env python
import webapp2
import caesar


class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = 'Hello world!!!!!!!!!'
        rot = 13
        encrypted_message = caesar.encrypt(message, rot)
        self.response.write(encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
