from functions import get ,write
import time
h=time.strftime("%b %d, %Y %H:%M:%S")
print("its now",h)
while True:
    user=input("enter add or show or edit or complete or exit:")
    user=user.strip()
    if user.startswith("add"):
             sai=user[4:]    
             a=get()
             a.append(sai+"\n")
             write(a)
    elif user.startswith("show"):
            a=get("thht.txt")
            for index,item in enumerate(a):
             item=item.strip("\n")
             print(index,'.',item)
    elif user.startswith("edit"):
        try:
            s=int(user[5:])
            print(s)
            s=s-1
            a=get()
            b=input("enter any todo:")
            a[s]=b+"\n"
            write(a)
        except ValueError:
                print("please write correctly")
                continue
    elif user.startswith("complete"):
        try:
            v=int(user[9:])
            a=get()
            a.pop(v-1)
            write(a)
        except IndexError:
                print("no such index is found")
                continue
    elif user.startswith("exit"):
            break
        
    else:
        print("please try again")
        
print('bye ra thammudu')
