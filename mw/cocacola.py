import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "magic.py" or file == "the.key" or file == "cocacola.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open("the.key","rb") as key:
	secretkey = key.read()
 


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)

