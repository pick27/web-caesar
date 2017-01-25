#!/usr/bin/env python
import webapp2
import cgi
import caesar


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = """
        <h2>Web Caesar</h2>
        <form method="POST">
        <label>Rotate by:<br />
        <input type="number" name="rot"/>
        </label>
        <p />
        """
        mainbox = """<label>Type a message:<br /><textarea name="message"
        style="height: 100px; width: 400px;"></textarea></label>
        """
        footer = """
        <p />
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
        <h2>Web Caesar</h2>
        <form method="POST">
        <label>Rotate by:
        <input type="number" name="rot" value="%s"/><br />
        </label>
        <p />
        """ % rot
        mainbox = """<label>Type a message:<br /><textarea name="message"
        style="height: 100px; width: 400px;">%s</textarea></label>
        """ % encrypted_message
        footer = """
        <p />
        <input type="Submit" />
        </form>
        """
        content = header + mainbox + footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
