#Create a hardcoded list of 8 numbers. Without using any loops, print:
#The first item
#The last item (use a negative index)
#A slice containing only the middle four items
#The full list in reverse order
number_list = [1, 33, 6, 2, 100, 0, 99, 200]
print (number_list[0]) #Output  first item
print (number_list[-1]) #Output last item
print (number_list[1:5]) #Output only the middle four items
number_list.reverse()
print (number_list)