def countFriendsPairings(n): 
  
    new= [0 for i in range(n + 1)] 
    for i in range(n + 1): 
  
        if(i <= 2): 
            new[i] = i 
        else: 
            #base case
            new[i] = new[i - 1] + (i - 1) * new[i - 2] 
  
    return new[n] 
    
if __name__ == "__main__":
    # n = 3
    n=int(input())
    l=[]
    for i in range(n):
        test_case=int(input())
        l.append(test_case)
    print("<---------------------output------------------------>")
    for i in l:
        print(countFriendsPairings(i)) 