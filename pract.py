names = ['a', 'b', 'c', 'd']
years = [1, 2, 3, 4]
x = zip(names, years)
count = 1
for i in x :
    print(f"set : {count}, data: {i}")
    count +=1

print("done!")

print(type(x))
chr = print(chr(65))
print(ord("A"))

print(int(True))
print(int(False))
print(int('10', 8))
print(10**10)
print(int(100_000))