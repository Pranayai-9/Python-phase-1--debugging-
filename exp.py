#without copy()
a = [10, 20, 30]
b = a.copy()

b.append(40)

print(a)
print(b)


#using copy()
a = [10, 20, 30]
b = a

b.append(40)

print(a)
print(b)

#Inference: Assigning 2 variables same object value results similar outputs like b=a, but instead making a copy one do not allow mutation.