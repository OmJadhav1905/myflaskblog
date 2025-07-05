from flask import Flask, render_template

app = Flask(__name__)

posts = {
    "first-post": {
        "title": "The 'I' Paradox – First Post",
        "content": "This is my first post exploring the mystery of self and existence."
    },
    "second-post": {
        "title": "The 'I' Paradox – Second Post",
        "content": "This is my second post diving deeper into self awareness."
    }
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post1')
def post1():
    return render_template('post1.html')

@app.route('/post/<post_name>')
def post(post_name):
    post = posts.get(post_name)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)


