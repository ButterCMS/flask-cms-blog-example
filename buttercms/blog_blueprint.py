from butter_cms import ButterCMS
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


blog = Blueprint('blog', __name__, template_folder='templates/blog')


auth_token = "YOUR_API_TOKEN"
client = ButterCMS(auth_token)


@blog.route('/')
@blog.route('/page/<int:page>')
def home(page=1):
    response = client.posts.all(page=page, page_size=10)
    posts = response['data'] 
    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']
    return render_template('blog.html', posts=posts, next_page=next_page, previous_page=previous_page)


@blog.route('/<slug>')
def show_post(slug):
    response = client.posts.get(slug)
    try:
        post = response['data']
    except:
        # Post was not found
        abort(404)
    return render_template('post.html', post=post)


@blog.route('/author/<author_slug>')
def show_author(author_slug):
    response = client.authors.get(author_slug, {'include':'recent_posts'})
    
    try:
        author = response['data']
        print author
    except:
        # Author was not found
        abort(404)
    return render_template('author.html', author=author)


@blog.route('/category/<category_slug>')
def show_category(category_slug):
    response = client.categories.get(category_slug, {'include':'recent_posts'})
    try:
        category = response['data']
        print category
    except:
        # category was not found
        abort(404)
    return render_template('category.html', category=category)


@blog.route('/rss')
def rss_feed():
    response = client.feeds.get('rss')
    return Response(response['data'], mimetype='text/xml')


@blog.route('/atom')
def atom_feed():
    response = client.feeds.get('atom')
    return Response(response['data'], mimetype='text/xml')


@blog.route('/sitemap.xml')
def sitemap():
    response = client.feeds.get('sitemap')
    return Response(response['data'], mimetype='text/xml')

