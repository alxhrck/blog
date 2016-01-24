import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import glob
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # If not needed. Set to True uses more memory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String(80), unique=True)
    text = db.Column(db.Text)

    def __init__(self, date, title, text):
        self.date = date
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Title %r>' % self.title


def add_blog_entry():
    mdfiles = glob.glob('posts/*.md')
    for md in sorted(mdfiles, reverse=True):
        with open(md, 'rb') as f:
            for i, line in enumerate(f):
                if i == 0:
                    title = line.split(' {')[0].strip('##')
                if i == 2:
                    date = datetime.strptime(line.strip(), "%B %d, %Y")
                    break
        with open(md, 'rb') as f:
            a = unicode(f.read(), 'utf8')
            text = Markup(markdown.markdown(a, ['markdown.extensions.extra']))

        p = Post(date, title, text)
        db.session.add(p)
    try:
        db.session.commit()
    except Exception as e:
        pass

@app.route('/')
def index():
    entries = dict()
    archives = list()

    posts = Post.query.all()
    for post in posts:
        #''.join(post.text.split('\n')[0:4])
        entries[post.id] = post.text
        archives.append(post.date)

    return render_template('index.html', entries=entries, archives=sorted(archives, reverse=True))


@app.route('/posts/<int:id>')
def expand_post(id=None):
    post = Post.query.filter_by(id=id).first()

    return render_template('expand.html', post=post.text)

if __name__ == '__main__':
    db.create_all()
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