

import hashlib


def md5(data):
    return str.lower(hashlib.md5(data.encode(encoding='UTF-8')).hexdigest())