import hashlib

m = hashlib.md5()
m.update(b'ghca@222')
print(m.hexdigest())