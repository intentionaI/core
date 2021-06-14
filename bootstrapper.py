import sys, os, requests

r = requests.get('https://raw.githubusercontent.com/pashaaaaaaa/core/main/version.json').json()

f = open("version.txt", "r")
vnum = f.read()

if os.path.isfile('core.py'):
    if vnum != r['version']:
        print('not updated, downloading the latest version...')
        f = open("version.txt", "w")
        f.write(r['version'])
        cr = requests.get('https://raw.githubusercontent.com/pashaaaaaaa/core/main/main.py').text
        cf = open('core.py', 'w')
        cf.write(cr)
        cf.close()
        exec(open('./core.py').read())
    else:
        exec(open('./core.py').read())
else:
    print("core.py doesn't exist... downloading...")
    f = open("version.txt", "w")
    f.write(r['version'])
    cr = requests.get('https://raw.githubusercontent.com/pashaaaaaaa/core/main/main.py').text
    cf = open('core.py', 'w')
    cf.write(cr)
    cf.close()
    exec(open('./core.py').read())
