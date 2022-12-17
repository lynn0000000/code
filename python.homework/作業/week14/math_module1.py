# factors(n)，用來傳回n的所有因數
def factors(n):
    lst=[]
    for i in range(1,n+1):
        if n%i ==0:
            lst.append(i)
    if True:
        print(lst)
#primes(n)，可用來傳回所有小於等於n的質數
def primes(n):
    lst=[]
    for i in range(1,n+1):
        times = 0
        for a in range(1,i+1):
            if i%a ==0:
                times+=1
                if times<=2 and a not in lst:
                    lst.append(a)
    if True:
        print(lst,end="")
