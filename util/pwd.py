import hashlib

salt = '**07##JohnnyLeung23%%29&&'


def password_md5(password):
    md5 = hashlib.md5(password.encode('utf-8'))
    md5.update(salt.encode('utf-8'))
    return md5.hexdigest()
