names = ['a', 'b', 'c', 'd']
years = [1, 2, 3, 4]
x = zip(names, years)
count = 1
for i in x :
    print(f"set : {count}, data: {i}")
    count +=1

print("done!")


