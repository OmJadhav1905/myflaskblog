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

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<blog_name>')
def blog(blog_name):
    blog = blogs.get(blog_name)
    if blog:
        return render_template('blog.html', blog=blog)
    else:
        return "Blog not found", 404

if __name__ == "__main__":
    app.run(debug=True)


