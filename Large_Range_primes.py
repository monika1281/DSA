
def rangePrime(a,b):
    p=[True]*(b-a+1)
    limit = (int(b**(1/2))+1)
    seive=[True]*(limit+1)
    prime=[]
    for i in range(2,limit):
        if seive[i]:
            prime.append(i)
            for j in range(i*i,limit,i):
                seive[j]=False
    for i in range(0,len(prime)):
        x = (prime[i]*2)
        while(x<a):
            x+=prime[i]
        for j in range(x,b+1,prime[i]):
            p[j-a]=False
    
    list1=[]
    for i in range(0,b-a+1):
        if p[i]:
            list1.append(i+a)
    return list1


t = int(input())
for _ in range(t):
    a,b= map(int,input().split())
    temp=(rangePrime(a,b))
    for i in temp:
        if i==1:
            pass
        else:
            print(i)
    print()
