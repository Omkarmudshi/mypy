#map, filter and lambda
def squre(num):

    return num**2
my_num=[1,2,3,4,5]
for i in map(squre,my_num):
    print(i)


print(list(map(squre,my_num)))



############################################################
#
def ene(mystring):
    if len(mystring)%2==0:
       return "even"
    else:
        return "false"

name=["omkar","omka"]
print(list(map(ene,name)))


##################################################################


names=["omak","kje"]
print(list(map(lambda name:name[0],names)))