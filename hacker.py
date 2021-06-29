import requests
import json

def cmd_prompt(string):
              url = "http://pytalk.c1.biz/cmd_post.php"
              data = {
                  "cmd": string
              }

              r2 = requests.post(url=url, data=data)

while True:
              check = input("show (y/n/q) : ")
              r = requests.get("http://pytalk.c1.biz/receive.php")
              if r.status_code == 200:
                            dic = json.loads(r.text)
                            
                            if dic["status"] == "0" and check == "y":
                                          #print(dic["output"])
                                          cmd = input(dic["output"])
                                          cmd_prompt(cmd)
                            elif check == "q":
                                          break
                            else:
                                          print("No Command")
              else :
                            print("check Internet Error")
                            


