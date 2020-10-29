n=input()
str=''
dict={'w':'q','e':'w','r':'e','t':'r','y':'t','u':'y','i':'u','o':'i','p':'o','[':'p',']':'[','s':'a','d':'s','f':'d','g':'f','h':'g','j':'h','k':'j','l':'k','l':';','x':'z','c':'x','v':'c','b':'v','n':'b','m':'n',',':'m','.':',','/':'.'}
for i in range(len(n)):
    if ord(n[i])>=65 and ord(n[i])<=90:
        str+=dict[n[i].lower()].upper()
    elif ord(n[i])>=97 and ord(n[i])<=122:
        str+=dict[n[i]]
    elif n[i]==' ':
        str+=' '
    else:
        str+=dict[n[i]]
print(str)
    
