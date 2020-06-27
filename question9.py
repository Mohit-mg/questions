  
def countWays(n, m): 
    count =[] 
    for i in range(n + 2): 
        count.append(0) 
    count[0] = 0
    for i in range(1, n + 1): 
      
        if (i > m): 
            count[i] = count[i-1] + count[i-m] 
            
        elif (i < m or i == 1):  
            count[i] = 1
  
        else: 
            count[i] = 2
      
    return count[n] 

 
if __name__ == "__main__":
    test_case=int(input())
    l=[]
    for _ in range(test_case):
        new=tuple(map(int,input().split()))
        l.append(new)
    print(l)
  
    for item in l:
        n,m=item
        
        print(countWays(n,m))
    