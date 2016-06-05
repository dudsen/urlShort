from urlShortCore import interfacein, interfaceout
from flask import Flask, redirect
import re 
def check(test_str): 
    pattern = r'[^a-fA-F0-9]'
    if re.search(pattern, test_str):
        return False
    else: 
        return True
app = Flask(__name__)
@app.route('/')
def home():
    return "urlshort \n"

@app.route('/u/<path:request>')
def urlret(request):
    if check(request):
        return redirect(interfaceout(request))
    else:
        return 'oops wrong\n'

if __name__ == "__main__":
    app.run(debug=True)

