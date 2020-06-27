# <------------------------------------------------------->
def factors(n):
    fact_list=[]
    n=int(n)
    for i in range(1,n+1):
        if n%i==0:
            fact_list.append(i)
    return fact_list

# <---------------------------------------------------------->
def checksum(num,fact_list):
    sum=0
    for i in fact_list:
        sum+=i
    if sum==num:
        return "yes"
    return 

# <------------------------------------------------------------>
def nums():
    for i in range(10000):
        yield(i)

number=nums()
def final(n):
    for num in number:
        var=factors(num)
        sub=checksum(n,var)
        if sub =="yes":
            return num


if __name__ == "__main__":
    num_list=[]
    start=1
    while start!=0:
        n=int(input())
        if n == 0:
            start=0
            break
        num_list.append(n)
    print("<-----------------output-------------------->")    
    for i in num_list:
        var=final(i)
        if var !=None:
            print(var)
        elif final(i)==None:
            print("-1")


    