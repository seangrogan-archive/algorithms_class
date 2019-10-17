def main():
    print('reccurance alg for TP1')
    x = 100
    #x = str(input('number: '))
    for i in range(x):
        q=t(i)
        y=t_2(i)
        print(i , ' , ' , q , ' , ' , y)
        if q != y:
            print('error at ',i)
    

def t(n):
    if n == 0:
        return n + 1
    elif n == 1:
        return 1 + n
    else:
        return 3*t(n-1)-2*t(n-2)+3*2**(n-2)
def t_2(n):
    return 3-2**(n+1)+3*n*2**(n-1)
main()
