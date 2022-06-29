stroke=input()
max=stroke[0]
for i in range(0,len(stroke)-1):
    for j in range(len(stroke),i,-1):
        comp=stroke[i:j]
        if comp == comp[::-1]:
            if len(max)<len(comp):
                max=comp
print(max)
