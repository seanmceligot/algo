from typing import *

def duplicateZeros(arr: List[int]) -> None:
	for i in range(len(arr)-1):
		if arr[i] == 0:
			tmp=arr[i+1]
			for j in range(i, len(arr)-1):
				tmp=arr[j+1]
				arr[j+1]=arr[j]

a = [1,0,2,3,0,4,5,0]
print(a)             
duplicateZeros(a )
print(a)
