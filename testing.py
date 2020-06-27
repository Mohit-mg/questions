# import numpy as np

# string=list(map(int,input().split()))
# string=sorted(string)


# def add()
# string=[1,3,2]
# substr=[]
# for i in range(len(string)):
#     for j in range(i,len(string)):
#         substr.append(string[i:j+1])

# print(substr)
# count=0
# for pos,item in enumerate(string):
#     sum=0
#     for j in range(0,len(string)):
#         try:
#             sum=string[pos]+string[j+pos]
#             # print(j)
#             # print(sum)
#             if sum==0:
#                 count+=1
#                 # print("yes")
#         except:
#             pass



# arr=np.array(substr)
# print(type(arr))
# print(arr)
# print(arr[7]+arr[9])
# count=0
# for item in substr:
#     for i in range(1,len(substr)):
#         if sum(substr[item],substr[i])==0:
#             count+=1
# print(count)
        

#2d array
# new_array=[[int(item)]for item in substr]
# print(new_array)
# output=[]
# for item in new_array:
#     for i in item:
#        if i>10:
#            t=i//10
#            m=i%10
#            if t>10:
#                r=t>10
#         output.append(t)
# print(output)


# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)

# n=5+1
# print(fibonacci(n))