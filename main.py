#!/usr/bin/env python
import webapp2
import caesar


class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = 'Hello world!!!!!!!!!'
        rot = 13
        encrypted_message = caesar.encrypt(message, rot)
        header = """
        <form method="GET">
        <label>Amount to rotate by:
        <input type="text" name="rot" />
        </label>
        <br />
        """
        boxes = '<textarea name="message" style="height: 100px; width: 400px;">' + encrypted_message + '</textarea>'
        footer = """
        <input type="Submit" />
        <br />
        </form>
        """
        content = header + boxes + footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
