def balckjack(*a):
    if  sum([*a])<= 21:
        return sum([*a])
    
    elif 11 in [*a] and sum([*a])<=31:
        sum1=sum([*a])-10
        return sum1

    else:
        return 'BUST'  

print(balckjack(9,9,11,20))