def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

if __name__ == "__main__":
    num_input=int(input())
    new_list=[]
    for i in range(num_input):
        n=list(map(int,input()))
        n=new_list.extend(n)

    print("<-------------------------output------------------->")
    for item in new_list:
        item=item+1
        print(fibonacci(item))