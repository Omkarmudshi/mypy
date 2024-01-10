def most_expancive(stock):
    current_max=0
    name_company=''

    for name,price in stock:
        if price > current_max:
            current_max = price
            name_company= name
        else:
            pass
    return (name_company,current_max)
a=[('apple',100),('mac',200)]
result= print(most_expancive(a))
