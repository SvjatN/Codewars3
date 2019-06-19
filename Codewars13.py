def create_array(n):
    res=[]
    i=1
    while i <= n: 
        res.append(i)
        i = i+1
    print(res)
    return res

print(create_array(5))