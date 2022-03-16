from flask import Flask, render_template, request, jsonify

import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    posts = utils.get_posts_all_from_json()
    comments = utils.get_comment_all_from_json()
    return render_template('index.html', posts=posts, comments=comments)


@app.route('/posts/<int:pk>')
def get_post(pk):
    post = utils.get_post_by_pk(pk)
    comments = utils.get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search')
def search_posts():
    s = request.args.get('s', '')
    posts = utils.search_for_posts(s)
    return render_template('search.html', posts=posts, s=s)


@app.route('/user-feed/<poster_name>')
def search_post_user(poster_name):

    poster_name = poster_name
    all_posts_user_name = utils.get_posts_by_user(poster_name)
    return render_template('user-feed.html', all_posts_user_name=all_posts_user_name, poster_name=poster_name)

@app.route('/api/posts')
def get_posts():
    posts = utils.get_posts_all_from_json()

    return jsonify(posts)

@app.route('/api/posts/<int:post_id>')
def get_posts_user(post_id):
    post = utils.get_post_by_pk(post_id)

    return jsonify(post)



if __name__ == "__main__":
    app.run()
