#Max from 3

def max_from_three(a,b,c):
    if a>b and a>c:
        return "a is MAX "
    elif b>a and b>c:
        return "b is MAX "
    elif c>a and c>b:  
        return "c is MAX "
    else:
        return "All numbers are equal."
    
    
    
a1 = int(input("a : "))
a2 = int(input("b : "))
a3 = int(input("c : "))

ans = max_from_three(a1,a2,a3)

print (ans)
# maxfrom three