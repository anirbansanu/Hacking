f = open("attack.txt", "rb")

string = f.read()
f.close()


f1 = open("a.txt", "wb")
f1.write(string)
f1.close()




