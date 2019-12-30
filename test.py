from fonAPI.fonAPI import FonApi
	
fon = FonApi('f36fc5968a418f32aca94157b7898c2cf296f189bcefa8de')
	
device = 'samsung galaxy s5 '
	
phones = fon.getdevice(device)
try:
	for phone in phones:
		print(phone['os'])
		print(phone['colors'])

except:
	print(phones)