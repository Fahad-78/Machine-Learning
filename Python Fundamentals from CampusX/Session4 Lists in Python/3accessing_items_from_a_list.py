#Indexing in 1D list
L = [1, 2, 3, 4, 5]
#Positive Indexing
print(L[0]) #target 1
#Negative Indexing
print(L[-1]) #target 5

#Indexing in 2D list
L = [1, 2, 3, [4, 5]]
#positive indexing
print(L[3][1]) #target 5
#negative indexing
print(L[-1][-2]) #target 4

#Indexing in 3D list
L = [[[1, 2], 3, 4], [5, [[6, 7], 8]]]
#positive indexing
print(L[0][0][1]) #target 2
#negative indexing
print(L[-1][-1][-2][-1]) #target 7



#Slicing
L = [1, 2, 3, 4, 5, 6]
print(L[0:3]) #First 3 items
print(L[-3:])  #Last 3 items
print(L[0::2])  #Jump items
print(L[-5:-2:2])  #Jump items
print(L[::-1]) #Reverse the list