given_string=input()
no_for_shifting_letters=int(input())
resulting_string=''
for i in range(len(given_string)):
    if ord(given_string[i])>=65 and ord(given_string[i])<=90:
        resulting_string+=chr(ord(given_string[i])+no_for_shifting_letters)
    elif ord(given_string[i])>=97 and ord(given_string[i])<=122:
        resulting_string+=chr(ord(given_string[i])+no_for_shifting_letters)
    elif given_string[i]==' ':
        resulting_string+=' '
    else:
        resulting_string+=given_string[i]
print(resulting_string)
