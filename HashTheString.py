import hashlib
s = "Python Bootcamp".encode('utf-8') #encoding before hashing required
print(hashlib.md5(s).hexdigest())
