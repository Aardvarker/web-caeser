import cgi
import os
import jinja2

template_dir = os.path.join(os.pth.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir),autoescape=True)

#form  becomes:
template = jinja_env.get_template(user_signup_template.html')
return template.renderer()

first_name = request.form['first_name']
template = jinja.env.get_template('user_signup_template.html')
return template.renderer(name=first_name)

