sum = 0

def add(i,n):
    global sum
    sum = sum + n
    i = i + 1
    if i <= 10:
        add(i,n+1)
    else:
        print(sum)
        return
add(1,1)
                    
