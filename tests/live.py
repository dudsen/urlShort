import requests
urlf = 'http://localhost:5000/'
with open('tests/hex.txt') as f:
    lines = f.read().splitlines()

failuretest = ['DROPDB','stupid','test','ffffff']

def testing(inList):
    for i in inList:
        r = requests.get(urlf + i, allow_redirects=False)
        print r.headers
        print r.content, r

testing(lines)
testing(failuretest)



