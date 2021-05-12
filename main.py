import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/86d86492a8a0483bb6ed")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<num>')
def blogpost(num):
    response = requests.get("https://api.npoint.io/86d86492a8a0483bb6ed")
    all_posts = response.json()
    post_number = int(num)-1
    return render_template("blogpost.html", posts=all_posts, num=num, post_number=post_number)


if __name__ == "__main__":
    app.run(debug=True)
