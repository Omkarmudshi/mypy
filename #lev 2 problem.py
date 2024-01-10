#lev 2 problem
def has_33(numbers):
    for i in range(len(numbers)):
        if numbers[i]==3 and numbers[i+1]==3:
            return True
    return False
print(has_33([1,2,3,4]))

def paper_doll(name):
    result=' '
    for char in name:
        result+=char*3
    return result
print(paper_doll('omkar'))



