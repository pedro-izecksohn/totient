def divisors (number):
    ret=[]
    curdiv = 2
    while curdiv < number:
        if (number%curdiv)==0:
            ret.append(curdiv)
            number = number//curdiv
        else:
            curdiv += 1
    ret.append(number)
    return ret

def lcm (a, b):
    if (a==0) or (b==0):
        return 1
    if a==b:
        return a
    elif a>b:
        a,b=b,a
    if (b%a)==0:
        return b
    divisor=1
    ret=1
    while (a!=1)or(b!=1):
        divisor+=1
        while ((a%divisor)==0) and ((b%divisor)==0):
            a//=divisor
            b//=divisor
            ret*=divisor
        while ((a%divisor)==0):
            a//=divisor
            ret*=divisor
        while ((b%divisor)==0):
            b//=divisor
            ret*=divisor
    return ret

n=int(input("Enter the number n: "))
l=divisors(n)
if len(l)!=2:
    print ("This number has",len(l),"divisors.")
    exit()
p=l[0]
q=l[1]
totient=lcm (p-1, q-1)
print ("totient="+str(totient))
