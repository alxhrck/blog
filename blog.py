import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import glob
from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import collections
from flask import redirect

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
    for md in mdfiles:
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
        if not Post.query.filter_by(title=title).first():
            p = Post(date, title, text)
            db.session.add(p)
    try:
        db.session.commit()
    except Exception as e:
        return 'no updates'
    return 'OK'


def archives_sidebar():
    archives = list()
    posts = Post.query.all()
    for p in posts:
        a = p.date.date().strftime("%Y")
        if a not in archives:
            archives.append(a)
    return sorted(archives, reverse=True)


@app.route('/<int:page>')
@app.route('/', defaults={'page': 1})
def index(page):
    e = dict()
    archives = list()
    next_pg = page + 1
    prev_pg = page - 1
    pages = Post.query.order_by(Post.id.desc()).paginate(page, 4, False)
    if page > pages.pages:
        return redirect(url_for('index'))

    for post in pages.items:
        e[post.id] = post.text
        archives.append(post.date)
    entries = collections.OrderedDict(sorted(e.items(), reverse=True))
    return render_template('index.html', entries=entries, archives=archives_sidebar(), next_pg=next_pg, prev_pg=prev_pg)


@app.route('/posts/<int:id>')
def expand_post(id=None):
    post = Post.query.filter_by(id=id).first()

    archives = list()
    posts = Post.query.all()
    for p in posts:
        a = p.date.date().strftime("%Y")
        if a not in archives:
            archives.append(a)

    return render_template('expand.html', post=post.text, archives=archives_sidebar())

@app.route('/<year>')
def archives_by_year(year=None):
    posts = Post.query.filter(Post.date.like('%' + year + '%')).all()
    entries = dict()
    for post in posts:
        entries[post.id] = post.text
    entries = collections.OrderedDict(sorted(entries.items(),  reverse=True))
    return render_template('index.html', entries=entries, archives=archives_sidebar())

@app.route('/update')
def update_blog():
    add_blog_entry()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
