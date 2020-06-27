def factorial(n):
    i=1
    a=1
    while n>=i:
        a*=i
        i+=1
    if n==1:
        return a
    return a

def max_x(n,k):
    x=0
    a=[]
    start=True
    while start:
        if factorial(n)%(k**x)==0:
            a.append(x)
            x+=1
        elif factorial(n)%(k**x)!=0:
            start=False
    a=max(a)
    return a


if __name__ == "__main__":
    test_case=int(input())
    current_case=0
    while(current_case<test_case):
        n,k=list(map(int,input().split()))
        current_case+=1
        a=max_x(n,k)
        print(a)