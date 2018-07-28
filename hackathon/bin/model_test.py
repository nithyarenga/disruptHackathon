from flask import Flask

app = Flask(__name__)

@app.route('/<string:groupid>')

def instagram_groupid(groupid=None):
    return("Current Group ID: {}".format(groupid))