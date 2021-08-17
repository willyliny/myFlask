from sys import is_finalizing
from flask import Flask, json, url_for,request,session
from flask import jsonify
from flask.helpers import make_response
from urllib.parse import urlparse, urljoin
from flask.templating import render_template
from werkzeug.utils import redirect
from werkzeug.wrappers import response
app = Flask(__name__)

user = {
    'username': 'Willy Lin',
    'age' : '22',
    'birth' : '88/04/25',
}

data = [
                        120,
                        134,
                        800,
                        700,
                        500]

movies = [
    {'name' : 'My Neighboor Totoro', 'year':'1988'},
    {'name' : 'Three Colours', 'year':'1993'},
    {'name' : 'Forrest Gump', 'year':'1994'},
    {'name' : 'Perfect blue', 'year':'1997'},
    {'name' : 'Memento', 'year':'1999'},
]

@app.route("/x")
def index():
    file_name = "hello, i am willy"
    return render_template('index.html',data=json.dumps(data))

# @app.route('/main')
# def mainPage():
#     return render_template('watch.html', user=user, movies = movies)

# @app.route('/foo')
# def foo():
#     return '<h1>Foo Page</h1><a href = "{}">Do something</a>'.format(url_for('do_something', next=request.full_path))

# @app.route('/bar')
# def bar():
#     return '<h1>Bar Page</h1><a href = "{}">Do something</a>'.format(url_for('do_something', next=request.full_path))

# @app.route('/do_something')
# def do_something():
#     return redirect_back()

# @app.route("/set/<name>")
# def set_cookie(name):
#     response = make_response(redirect(url_for('hell')))
#     response.set_cookie('name',name)
#     return response

# def redirect_back(default='hell', **kwargs):
#     for target in request.args.get('next'), request.referrer:
#         if not target:
#             continue
#         if is_safe_url(target):
#             return redirect(target)
#     return redirect(url_for(default, **kwargs))

# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and \
#         ref_url.netloc == test_url.netloc

if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000)