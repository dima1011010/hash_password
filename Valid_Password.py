# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import re
import hashlib

password = input()
flag = True
passwd = hashlib.sha256(password.encode())
convert = passwd.hexdigest()

while True:
    if(len(password) < 8):
        flag = False
    elif not re.search("[a-z]", password):
        flag = False
    elif not re.search("[A-Z]", password):
        flag = False
    elif not re.search("[0-9]",password):
        flag = False
    elif not re.search("[_@$]", password):
        flag = False
    elif not re.search("[\s]", password):
        flag = False
    else:
        print(convert)
        break
    if flag == False:
        print("Not a valid password")
        break
    