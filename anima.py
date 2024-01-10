def animal_cracker(text1,text2):
    if text1[0]==text2[0]:
        return True
    else:
        return False

print(animal_cracker("omkar","oagar"))


def another(text):
    worldlist=text.split()
    print(worldlist)

    first=worldlist[0]
    second=worldlist[1]
    if first[0]==second[0]:
        print( True)
    else:
        print (False)
    
another("omkar oudshi")

def another(text):
    worldlist=text.lower().split()
    return worldlist[0][0]==worldlist[1][0]    
another("omkar Oudshi")


def make_twenty(n1,n2):
    return n1+n2==20 or n1==20 or n2==20
#
    if n1==20 or n2==20:
        print("one of other is 20")
        return True
    elif n1 + n2 ==20:
        print("addition of both is 20")
        return True
    else:
        print("Nither one is 20 or addition of both is 20")
        return False
print (make_twenty(10,1))




def master_yoda(text1):
    wordlist=text1.split()
    revwords=(wordlist[::-1])
    return ' '.join(revwords)
print(master_yoda("hii im om"))
