# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import glob
from random import randint
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    entries = list()
    archives = list()
    posts = glob.glob('posts/*.md')
    for post in sorted(posts, reverse=True):
        with open(post, 'rb') as f:
            ts = f.name.split('/')[1].split('-')[0]  # get the date stamp from the posts filename
            arc_date = datetime.strptime(ts, "%Y%m%d")

            if arc_date not in archives:
                archives.append(arc_date)

            p = f.read()
            content = dict()
            content['id'] = randint(0,1000)
            content['text'] = Markup(markdown.markdown(unicode(p, 'utf8'), ['markdown.extensions.extra']))
        entries.append(content)

    return render_template('index.html', entries=entries, archives=sorted(archives, reverse=True))

if __name__ == '__main__':
    app.run(debug=True)




### Code to convert dates in posts to dates used in filename
#from datetime import datetime
#post_date = p.split('\n')[2]
#fmt_post_date = list()
#try:
#    s = datetime.strptime(post_date, "%B %d, %Y")
#    new_date = s.strftime("%Y%m%d")
#    fmt_post_date.append(new_date)
#except ValueError:
#    print f.name
#filename = new_date + '-' + f.name.split('/')[1]
#with open(filename, 'wb') as nf:
#    nf.write(p)
#print sorted(fmt_post_date, reverse=True)