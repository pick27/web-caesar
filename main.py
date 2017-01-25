#!/usr/bin/env python
import webapp2
import cgi
import caesar


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = """
        <form method="POST">
        <label>Amount to rotate by:
        <input type="text" name="rot"/>
        </label>
        <br />
        """
        mainbox = """<textarea name="message"
        style="height: 100px; width: 400px;"></textarea>
        """
        footer = """
        <br />
        <input type="Submit" />
        </form>
        """
        content = header + mainbox + footer
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = self.request.get("rot")
        if message and rot.isdigit():
            encrypted_message = caesar.encrypt(message, int(rot))
        else:
            encrypted_message = message
        encrypted_message = cgi.escape(encrypted_message, quote=True)
        header = """
        <form method="POST">
        <label>Amount to rotate by:
        <input type="text" name="rot" value="%s"/>
        </label>
        <br />
        """ % rot
        mainbox = """<textarea name="message"
        style="height: 100px; width: 400px;">%s</textarea>
        """ % encrypted_message
        footer = """
        <br />
        <input type="Submit" />
        </form>
        """
        content = header + mainbox + footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
