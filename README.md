# ButterCMS Flask Example

## Important Notice
This project was created as an example use case of ButterCMS and Flask and will not be actively maintained. 

If you’re interested in exploring the best, most up-to-date way to integrate Butter into Python Frameworks like Flast, you can check out the following resources:

### Starter Projects

The following turn-key starters are fully integrated with dynamic sample content from your ButterCMS account, including main menu, pages, blog posts, categories, and tags, all with a beautiful, custom theme with already-implemented search functionality. All of the included sample content is automatically created in your account dashboard when you sign up for a free trial of ButterCMS.
- [Python Starter](https://buttercms.com/starters/python-starter-project/)
- [Angular Starter](https://buttercms.com/starters/angular-starter-project/)
- [React Starter](https://buttercms.com/starters/react-starter-project/)
- [Vue.js Starter](https://buttercms.com/starters/vuejs-starter-project/)
- Or see a list of all our [currently-maintained starters](https://buttercms.com/starters/). (Over a dozen and counting!)

### Other Resources
- Check out the [official ButterCMS Docs](https://buttercms.com/docs/)
- Check out the [official ButterCMS API docs](https://buttercms.com/docs/api/)

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
