a=[1,2,3,55,555,67,88]
mini=a[0]
max=a[0]

for i in range(len(a)):
    if a[i]<mini:
        mini=a[i]
    
    if a[i]>max:
        max=a[i]
        
print(mini,max)