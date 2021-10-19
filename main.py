



class CRC:
	
	def __init__(self):
		self.cdw = ''

	def xor(self,a,b):
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')


		return  ''.join(result)



	def crc(self,message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = self.xor(key,tmp)+message[pick]
			else:
				tmp = self.xor('0'*pick,tmp) + message[pick]

			pick+=1

		if tmp[0] == "1":
			tmp = self.xor(key,tmp)
		else:
			tmp = self.xor('0'*pick,tmp)

		checkword = tmp
		return checkword

	def encodedData(self,data,key):
		l_key = len(key)
		append_data = data + '0'*(l_key-1)
		remainder = self.crc(append_data,key)
		codeword = data+remainder
		self.cdw += codeword
		print("Data Remainder is : " ,remainder)
		print("Transmitted Value is : " ,codeword)

#have to edit this side 
	def reciverSide(codeword,key,data):
		r = codeword.crc(data,key)
		size = len(key)
		print("remainder:", r)
		if r != 0:
			print("Transmitted Error")
		else:
			print("Transmitted Successfully ")

print("welcome to CRC calculator, Input your Key and Data ,For learning more visit readme part ")
data = input("Input data\n")
key = input("Input key\n")

print('------ sender side ---------')
c = CRC()
c.encodedData(data,key)
print('------ reciver side ---------')
c.reciverSide(c.cdw,key)
print('---------------')
print("Reciver Get data: ",c.cdw)



