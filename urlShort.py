from urlShortCore import interfaceout
from flask import Flask
from flask import redirect
import re 


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

@app.route('/<path:request>')
def urlret(request):
    """returns url redict if key is a hex number and exist in db"""
    if check(request):
        val = interfaceout(request)
        if val:
            return redirect(val)
        return 'not fount', 404
    else:
        return 'stop doing stupid things\n', 403

if __name__ == "__main__":
    app.run(debug=True)

