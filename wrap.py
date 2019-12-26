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
try:
  os.remove("README.md")
except:
  pass
os.system("git init")
os.system("git remote add origin https://github.com/erenmetesar/NiceGrill.git")
os.system("git config branch.master.remote origin && git config branch.master.merge refs/heads/master")
os.system("git pull")
subprocess.call("pip install --upgrade -r https://raw.githubusercontent.com/erenmetesar/NiceGrill/master/requirements.txt".split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
file = open("client_secret.json", "w")
file.write(os.environ.get("client_secret", ""))
file.close()
import nicegrill
