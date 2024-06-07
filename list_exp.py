x= [10, -5, 9, 23, 12, 1]

x.append("Reza")
x.append(23)
x.append(12)

x.remove("Reza")
x.remove(9)
for i in range(0, len(x)):
    if x[i]== 1:
        x[i]= "ali"

print(x)