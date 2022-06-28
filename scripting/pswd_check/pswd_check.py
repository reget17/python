import requests
import hashlib
import sys


def get_response(*args):
    for pswd in args:
        head_pswd, tail_pswd = sha1_encode(pswd)
        url = 'https://api.pwnedpasswords.com/range/' + head_pswd
        response = requests.get(url)
        check_password(response, tail_pswd, pswd)
        

def sha1_encode(password):
    hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(hash)
    head = hash[:5]
    tail = hash[5:]
    return head, tail

def check_password(response, hash, password):
    hashes = (line.split(':') for line in response.text.splitlines())
    for pswd, count in hashes:
        if pswd == hash:
            return print(f'You should change your password. Password "{password}": {count} times')
    return print(f'Your password {password} is best')   

# get_response(sys.argv[1:])
get_response('password')
