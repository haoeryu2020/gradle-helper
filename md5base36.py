import hashlib

def get_md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def get_digest_size(str):
    #attribute 'digest_size' of '_hashlib.HASH' objects is not writable
    m = hashlib.md5()
    m.update(str)
    return m.digest_size

def get_block_size(str):
    m = hashlib.md5()
    m.update(str)
    return m.block_size

#http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python
import string
digs = string.digits + string.letters
def int2base(x, base):
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def get_md5b36(str):
    return int2base(int(get_md5(str), 16), 36)

def get_md5buu(str, base):
    return int2base(int(get_md5(str), 16), base)

