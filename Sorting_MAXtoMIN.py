# this example teach u how to reorder a list from max element to min element
# fun1 : find out the max value
global b 
b = []
def max(a):
   i = 0
   max = a[i]
   while i < len(a)-1:
       if max <= a[i+1]:
           max = a[i+1]
       i = i+1
   a.remove(max) # pick up max value and remain a new unsorting list
   return max # output max
# fun2 : call fun1 to find 1st max, 2md max, 3rd max.... and order them
def sort(a):
    b.append(max(a))
    if len(a) > 1:
        return sort(a)
    elif len(a) == 1:
        b.append(a[0])
        return b

a = [2134,2134,2134,8723,9239,1234,2345]
print("Import list: ",a)
print("Sorting result: ",sort(a))
