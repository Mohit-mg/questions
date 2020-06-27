from question3 import factorial

if __name__ == "__main__":
    n,r=map(int,input().split())
    output=factorial(n)/(factorial(r)*factorial(n-r))
    output=int(output)
    print(output)