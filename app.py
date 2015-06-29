import pymongo
from pymongo import MongoClient
from flask import request, Flask, render_template
import datetime
app = Flask(__name__)

client = MongoClient('localhost', 27017)

@app.route('/')
def mongo_list():
    db = client.flask_database
    collection = db.flask_collection
    posts = db.posts
    entries = posts.find()
    return render_template('index.html', entries = entries)

@app.route('/insert', methods=['POST'])
def mongo_insert():
    db = client.flask_database
    collection = db.flask_collection
    term = request.form['term']
    definition = request.form['definition']
    post = {"post_term": term,
            "post_definition": definition,
            "post_created": datetime.datetime.now()
            }
    posts = db.posts
    post_id = posts.insert(post)
    return render_template('list.html', term=term, definition=definition)

if __name__ == '__main__':
    app.run(debug=True)


