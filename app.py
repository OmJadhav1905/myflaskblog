from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

if __name__ == "__main__":
    app.run(debug=True)


