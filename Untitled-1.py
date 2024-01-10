def myfunc(st):
    result=''
    for i,char in enumerate(st):
        if i%2==0:
            result+=(char.upper())
        else:
            result+=char.lower()
    return(result)

print(myfunc("Arbitary"))    