import requests
urlf = 'http://localhost:5000/u/'
with open('tests/hex.txt') as f:
    lines = f.read().splitlines()
print lines

for i in lines:
    r = requests.get(urlf + i, allow_redirects=False)
    print r.headers
    print r.content
