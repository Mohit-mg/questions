def sorting(l):
    for pos,item in enumerate(l):
        try:
            if item in l[pos+1]:
                string=item
                l[pos]=l[pos+1]
                l[pos+1]=string
        except:
             return l


if __name__ == "__main__":
    n=int(input())
    new=[]
    for i in range(n):
        string=input()
        new.append(string)
    new.sort()
    new=sorting(new)
    print("<-----------------------------output--------------------------------->")
    for i in new:
        print(i)

    
