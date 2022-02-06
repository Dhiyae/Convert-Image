import os

os.system('clear')

os.system('apt update -y')

os.system('apt upgrade -y')

os.system('apt anstall jp2a')

os.system('clear')

os.system('termux-setup-storage -y')

os.system('clear')

os.system ('figlet termux-dz')

i = input ("\033[1;32mEnter the image path : \033[1;36m ")

os.system('jp2a '+i)