#Program 1
def div(a,b):#step 6
    print("a/b:",a/b)#step 7

def funct1(func): #step 2 func = div

    def innerFunct(a,b):#step 4
        if a<b:
            a,b = b,a

        func(a,b)#step 5
        print("Done")#step 8
    return innerFunct #step 3 div = innerFunct because from step 3
div=funct1(div) #step 1
div(2,4)#it will call innerFunct(a,b) ratherthen div(a,b) because of step 2

#Program 2 : Standardize MobileNumber Using Decorator
def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun
 sort_phone=wrapper(sort_phone)
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


