from flask import Flask, render_template, abort, Response
from buttercms.blog_blueprint import blog

app = Flask(__name__)

app.register_blueprint(blog, url_prefix='/blog')


@app.route('/')
def hello_world():
    return '''Homepage of our sample app.
    Set your ButterCMS token as BUTTERCMS_API_TOKEN env var then go to /blog'''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
