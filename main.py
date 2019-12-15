import os
os.remove("requirements.txt")
os.system("git init")
os.system("git remote add origin https://github.com/erenmetesar/NiceGrill.git")
os.system("git config branch.master.remote origin && git config branch.master.merge refs/heads/master")
os.system("git pull")
os.system("pip install -r requirements.txt")
config = open("config.py", "w")
config.write("API_ID = " + os.environ.get("API_ID", "1234") + "\nAPI_HASH = " + repr(os.environ.get("API_HASH", "1234")))
file = open("client_secret.json", "w")
file.write(os.environ.get("client_secret", ""))
file.close()
import nicegrill
