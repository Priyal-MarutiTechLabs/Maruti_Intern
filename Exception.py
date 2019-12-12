#exception handling
a = [1,2,3,4]
try:
    print("second element: %d"%a[2])
    print("Fifth element : %d" %a[5])
except IndexError:
    print('An error occured')

#raise
try:
    raise NameError("Hey,There!")
except NameError:
    print("An Exception")
    raise

#try-finally clause
try:
    fh=open("text",'w')
    try:
        fh.write("This is text file in exception handlling")
    finally:
        print("I am going to close my file")
        fh.close()
except IOError:
    print("Error: can't find file or read data")
else:
    print("File open succesfully")
