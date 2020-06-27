def output(string):
    count=0
    for pos,item in enumerate(string):
        sum=0
        for j in range(0,len(string)):
            try:
                sum=string[pos]+string[j+pos]
                # print(j)
                # print(sum)
                if sum==0:
                    count+=1
                    # print("yes")
            except:
                pass
    return count

class NotValidArray(ValueError):
    pass

if __name__ == "__main__":
    test_case=int(input())
    for _ in range(test_case):
        num_element=int(input())
        string=list(map(int,input().split()))
        if num_element == len(string):
            n=output(string)
            print("<--------------------output------------------->")
            for _ in range(n):
                print("Yes")
        else:
            raise NotValidArray("your array input not valid ")
  