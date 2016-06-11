from urlShortCore import interfaceout, interfacein
from flask import Flask
from flask import redirect
from flask import request
from validators import url as testurl
import re 
from os import getcwd

def check(test_str): 
    """checks if input loos like a hex number basic imput sanitation"""
    pattern = r'[^a-fA-F0-9]'
    if re.search(pattern, test_str):
        return False
    else: 
        return True

app = Flask(__name__)

@app.route('/')
def home():
    """just the home folder"""
    return "urlshort \n"


@app.route('/<path:req>')
def urlret(req):
    """returns url redirect if key is a hex number and exist in db"""
    if check(req):
        val = interfaceout(req)
        if val:
            return redirect(val)
        return 'not fount', 404
    else:
        return 'stop doing stupid things\n', 403


@app.route('/create', methods=["POST"])
def insert():
    print getcwd()
    app.logger.debug(request.json)
    if request.json:
        mydata = request.json  # will be
        print mydata
        if testurl(mydata.get("url")):
            return interfacein(mydata.get("url"))
        else:
            return 'arent you a naugty one', 403
    else:
        return "no json received", 500

if __name__ == "__main__":
    app.run(debug=True)
