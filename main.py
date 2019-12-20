import os, subprocess
try:
  os.remove("requirements.txt")
except:
  pass
try:
  os.remove("runtime.txt")
except:
  pass
try:
  os.remove("Procfile")
except:
  pass
os.system("git init")
os.system("git remote add origin https://github.com/erenmetesar/NiceGrill.git")
os.system("git config branch.master.remote origin && git config branch.master.merge refs/heads/master")
os.system("git pull")
subprocess.call("pip install -r https://raw.githubusercontent.com/erenmetesar/NiceGrill/master/requirements.txt".split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
config = open("config.py", "w+")
config.write("API_ID = " + os.environ.get("API_ID", "1234") + "\nAPI_HASH = " + repr(os.environ.get("API_HASH", "'1234'")) + "SESSION='" + str(os.environ.get("SESSION")) + "'")
config.close()
file = open("client_secret.json", "w")
file.write(os.environ.get("client_secret", ""))
file.close()
import nicegrill
