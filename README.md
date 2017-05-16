# ButterCMS Flask Example

## Documentation

For a comprehensive list of examples, check out our [documentation](https://buttercms.com/docs/).

## Get Started

This is a sample flask application that uses ButterCMS to power it's blog. 

1. Clone this repository.
2. `pip install -r requirements.txt`
3. Update `auth_token = "YOUR_API_TOKEN"` in `buttercms/blog_blueprint.py`  (Get a free token by registering on https://buttercms.com/)
4. `export FLASK_APP=app.py`
5. `flask run`

## Use on your app

Simply copy the `buttercms` folder into your app and register it as a blueprint:

```
# In app.py
from flask import Flask
from buttercms.blog_blueprint import blog

app = Flask(__name__)

app.register_blueprint(blog, url_prefix='/blog')
```

Configure the API key in `buttercms/blog_blueprint.py` and then go to /blog to see your blog posts on ButterCMS appear in your app. 

It's that easy!

### Other

View Flask [Blog engine](https://buttercms.com/flask-blog-engine/) and [Full CMS](https://buttercms.com/flask-cms/) for other examples of using ButterCMS with Flask.
