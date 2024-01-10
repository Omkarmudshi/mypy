#functions and methods
def vol(rad):
    return 4/3*3.14*rad**3
print(vol(2))

#################################

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f" {num} is in range of {low} and {high}")
    else:
        print("not in range")
print(ran_check(5,2,7))

###################################


def check_letter(sen):
    upper=0
    lower=0
    for i in sen:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print(f"{upper}")
    print(f"{lower}")
sample_string="woefuhw oefh JHOIE OEWFI "
print(check_letter(sample_string))


