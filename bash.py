import os
while True:
    os.fork()
    os.system("python server.py")