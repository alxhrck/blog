import glob
import markdown
import collections
from flask import Flask
from flask import render_template
from flask import Markup
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # If not needed. If set to True uses more memory
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
    entries = dict()
    next_pg = page + 1
    prev_pg = page - 1
    pages = Post.query.order_by(Post.id.desc()).paginate(page, 4, False)
    if page > pages.pages:
        return redirect(url_for('index'))

    for post in pages.items:
        entries[post.id] = (post.text, post.title)

    entries = collections.OrderedDict(sorted(entries.items(), reverse=True))
    return render_template('index.html', entries=entries, archives=archives_sidebar(), next_pg=next_pg, prev_pg=prev_pg)


@app.route('/posts/<int:id>/<title>')
def expand_post(id, title):
    post = Post.query.filter_by(id=id).first()

    return render_template('expand.html', post=post.text, archives=archives_sidebar())


@app.route('/archives/<year>/<int:page>')
@app.route('/archives/<year>/', defaults={'page': 1})
def archives_by_year(year, page):
    #posts = Post.query.filter(Post.date.like('%' + year + '%')).all()
    entries = dict()

    next_pg = page + 1
    prev_pg = page - 1
    pages = Post.query.filter(Post.date.like('%' + year + '%')).order_by(Post.id.desc()).paginate(page, 4, False)
    if page > pages.pages:
        return redirect(url_for('index'))

    for post in pages.items:
        entries[post.id] = post.text
    entries = collections.OrderedDict(sorted(entries.items(),  reverse=True))
    return render_template('index.html', entries=entries, archives=archives_sidebar(),
                           next_pg='archives/' + year + '/' + str(next_pg),
                           prev_pg='archives/' + year + '/' + str(prev_pg))

@app.route('/update')
def update_blog():
    db.create_all()
    mdfiles = glob.glob('posts/*.md')
    for md in sorted(mdfiles):
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
            existing = Post.query.filter_by(title=title).first()
        if not existing:
            p = Post(date, title, text)
            db.session.add(p)
        else:
            existing.text = text
            db.session.commit()

    try:
        db.session.commit()
    except Exception as e:
        pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
