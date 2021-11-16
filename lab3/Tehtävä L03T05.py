luku1=int(input("Anna 1 luku"))
luku2=int(input("Anna 2 luku"))
luku3=int(input("Anna 3 luku"))
luku4=int(input("Anna 4 luku"))
luku5=int(input("Anna 5 luku"))

if luku1<0:
    print (luku2+luku3+luku4+luku5)
elif luku2<0:
    print (luku1+luku3+luku4+luku5)
elif luku3<0:
    print (luku1+luku2+luku4+luku5)
elif luku4<0:
    print (luku1+luku2+luku3+luku5)
elif luku5<0:
    print (luku1+luku2+luku3+luku4)

elif luku1>0 and luku2>0 and luku3>0 and luku4>0 and luku5>0:
    print (luku1+luku2+luku3+luku4+luku5)