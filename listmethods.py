alist = [10,20,30,40]

print(alist)

alist.append(50)
alist.append(80)

print("After append",alist)

alist.extend([100,200,300])
print("After extend",alist)

print("number of occue of 10 is", alist.count(10))

alist.insert(0,3)
print(alist)

removed=alist.pop(0)
print(removed)

alist.reverse()
print("After reverse", alist)
