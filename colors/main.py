import color


print("List of colors")
for i in range(0,len(color.colors1)):
    print(str(i)+" "+str(color.colors1[i]))

chose = input("Birini tanlang :")

for i in range(0,len(color.colors1)):
    print(color.colors2[int(chose)])
    break
print("Hello")