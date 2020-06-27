def perm1(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l

if __name__ == "__main__":
    string=input()
    data=list(string)
    # print("perm1")
    new=[]

    for p in perm1(data):
        p=(",").join(p)
        p=p.replace(",","")
        new.append(p)

        # print(p)
    new=set(new)
    new=sorted(new)
    print(new)