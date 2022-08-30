from flask import Flask, render_template, url_for


app = Flask(__name__)


posts = [
    {
        'author': 'Angelo Bijoux',
        'title': 'Blog_post 1',
        'content': 'First post content',
        'date_posted': 'August 30 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog_post 2',
        'content': 'Second post content',
        'date_posted': 'August 31 2022'
    },
]


#multiple route decoraters can be served by the same function as below

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)