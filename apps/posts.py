# coding:utf-8
from flask import Blueprint, render_template, g

posts = Blueprint('posts', __name__)


@posts.route('/post/<int:post_id>')
@posts.route('/post/<int:post_id>/<slug>')
def view_post(post_id, slug=None):
    db = g.mongo.db
    post = db.posts.find_one_or_404({'_id': post_id})
    return render_template('post/view.html', post=post)