#import array module
from array import *
a=array("i",[1,2,34,5,55])
for x in a :
    print(x)    
#accessing    
print(a[0])
#inserting
a.insert(1,23)
#removing
a.remove(55)
#searching    
print(a.index(1)) 
#updating
a[2]=40
