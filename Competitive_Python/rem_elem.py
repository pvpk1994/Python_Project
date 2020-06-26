# find the remaining
def find_pair(list_elements: list, k: int)->int:
	# Convert list into a set
	counter = 0 
	set_elements = set(list_elements)
	for element in set_elements:
		result = element + k
		if result in set_elements:
			counter += 1
	return counter

if __name__== '__main__':
	k = int(input())
	list_elem = list(map(int, input().rstrip().split()))
	print("Counter is: " + str(find_pair(list_elem, k)))
