def available_sizes(ls):
    sizes = dict()
    for i in ls:
        if i in sizes:
            sizes[i]=sizes[i]+1
        else:
            sizes[i]=1
    return(sizes)

a = input().strip()
ls = input().split()

available = available_sizes(ls)
sum = 0
for i in range(int(input().strip())):
    order = input().split()
    size = order[0]
    price = order[1]
    if size in available and available[size]>0:
        available[size]-=1
        sum += int(price)
print(sum)

