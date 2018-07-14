# this example teach u how to make use of Lambda expression
# function1 in def expression:
def add(x,y):
    return x+y
print("def1 gives: ",add(3,4))

# fun1 Lambda expression:
Add = lambda x,y : x+y
print("Lambda1 gives: ",Add(5,6))

#---------------------------------------------------------------#

# function2 : find out the odd numbers
def odd(x):
    return x % 2 # which retrun 0(=false) or 1 (=true)
print("def2 gives: ",list(filter(odd,range(10))))

# fun2 in Lambda expression:
show = list(filter(lambda x : x % 2, range(13))) # filter() will remain true- or 1- items
print("Lambda2 gives: ",show)

#---------------------------------------------------------------#

# function3 : create corresponding list by map()
import numpy as np
def new(x):
    return 2*x
a = np.arange(10)
print("def3 gives: ",new(a))

#fun3 in Lambda expression:
print("Lambda3 gives: ",list(map(lambda x : 2*x , np.arange(13))))
