print("=============================================================================")
print("set and List")
print()

m = set()
print ("set m",m)
m.add("1111")
print ("set m",m)
m.add("2222")
print ("set m",m)
m.add("1111")
print ("set m",m)

l = [1,2,3,4,5,3,2,5,323,452,234]
print("List l", l)
print("set from l", set(l)) # delete repeat values
print("list l from set",list(set(l)))

m=set([1,2,3,4,5])
c=set([3,5,9])

print ("m=",m,"c=",c)
print ("set union ", m.union(c))
print ("set intersection ", m.intersection(c))
print ("set issubset 0-10", c.issubset(range(0,10)))

