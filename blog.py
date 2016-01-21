# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup
from flask import send_from_directory
import glob
from random import randint
import os

app = Flask(__name__)

@app.route('/')
def index():
    entries = list()
    posts = glob.glob('posts/*.md')
    posts.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    for post in posts:
      with open(post, 'rb') as f:
        content = dict()
        content['id'] = randint(0,1000)
        content['text'] = Markup(markdown.markdown(unicode(f.read(), 'utf8'), ['markdown.extensions.extra']))
      entries.append(content)

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)