import requests, json
from colorama import Fore, init
import os
from os import system
init()
def open_win():
    system("mode 65, 30")
    system("title [ https://github.com/MrLyes ]")

def main(name):
	pseu = 0
	code = requests.get("https://api.ashcon.app/mojang/v2/user/" + name).status_code #Request name data
	if code == 200:
		resp = requests.get("https://api.ashcon.app/mojang/v2/user/" + name)		
		data = json.loads(resp.text)
		print(f"[{Fore.GREEN}*{Fore.LIGHTWHITE_EX}] Pseudo: " + data["username"])
		print(f"[{Fore.GREEN}*{Fore.LIGHTWHITE_EX}] UUID: " + data["uuid"])
		if data["created_at"] == None:
			print(f"[{Fore.RED}-{Fore.LIGHTWHITE_EX}] Created the: Not found")
		else:
			print(f"[{Fore.GREEN}*{Fore.LIGHTWHITE_EX}] Created the: " + data["created_at"])
			print(f"\n[{Fore.GREEN}+{Fore.LIGHTWHITE_EX}] Name History: \n")
		for username in data["username_history"]: #Get username history
			pseu = pseu + 1
			try:
				chang = username["changed_at"].replace('T', ' at ').replace('.000Z', '')
				print(f'{Fore.GREEN}   =>  [{pseu}] {Fore.LIGHTWHITE_EX}{username["username"]} (Changed {chang})')
			except:
				chang = data["created_at"]
				print(f'{Fore.GREEN}   =>  [{pseu}] {Fore.LIGHTWHITE_EX}{username["username"]} (Frist Name)')
	else:
		print(f"[{Fore.RED}-{Fore.LIGHTWHITE_EX}] This pseudo does not exist")
open_win()
while True:
	os.system('cls')
	minecraft_name = input(f"[{Fore.GREEN}>{Fore.LIGHTWHITE_EX}] Pseudo Minecraft : ")
	main(minecraft_name)
	input('\nPress [Enter] For Retry')
