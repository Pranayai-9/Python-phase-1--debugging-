#using copy()
a = [10, 20, 30]
b = a.copy()

b.append(40)

print(a)
print(b)


#without copy()
a = [10, 20, 30]
b = a

b.append(40)

print(a)
print(b)

#Inference: Assigning 2 variables same object value results similar outputs like b=a because both variables point one single object, but instead making a copy one do not allow mutation because copy creates a seperate duplicate of the original.