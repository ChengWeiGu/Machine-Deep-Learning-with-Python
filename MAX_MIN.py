# this example teach u how to find out the max or min of numbers in a list
# fun1 : find out the max value
def MAX(a):
   i = 0
   max = a[i]
   while i < len(a)-1:
       if max < a[i+1]:
           max = a[i+1]
       i = i+1
   return max
# fun2 : find out the min value
def MIN(a):
    i = 0
    min = a[i]
    while i < len(a)-1:
        if min > a[i+1]:
            min = a[i+1]
        i += 1
    return min

a = [2134,3412,6421,8723,9239,1234,2345]
print("the import list is: ", a)
max = MAX(a)
min = MIN(a)
print("the max element : %d\nthe min element : %d" % (max,min))
