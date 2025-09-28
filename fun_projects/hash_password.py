import hashlib

def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_obj = hashlib.sha512()
    hash_obj.update(password_bytes)
    hashed_password = hash_obj.hexdigest()
    return hashed_password

password = str(input())
hashed_pasword = hash_password(password)
print(hashed_pasword)