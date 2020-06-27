

if __name__ == "__main__":
    size=int(input())
    array1=list(map(int,input().split()))
    array2=list(map(int,input().split()))
    if (len(array1) and len(array2))!=size:
        raise NotImplementedError("You have to enter valid input") 
    else:
        array=array1+array2
        array.sort()
        output=len(array)/2
        output=int(output)

    print("<--------------output---------------------->") 
    print(array[output-1])