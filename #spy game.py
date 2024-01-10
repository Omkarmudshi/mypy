#spy game
def spy_game(*arr):
    code=[0,0,7,'x']
    for i in arr:
        if i == code[0]:
            code.pop(0)
    return len(code)==1
print(spy_game(1,2,3,0,4,8,7,0))

#count primes

def prime(num):
    l1=[2]
    x=3
    while x<=num:
        for i in range(3,num,2):
            if i%num==0:
                print(f"prime{i}")
                break
            else:  
                    l1.append(x)
                    x+=2
    return l1

print(prime(10))