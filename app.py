from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html',posts=posts)

# @app.route('/about')
# def about():
  #  return render_template('about.html')

  #  return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
