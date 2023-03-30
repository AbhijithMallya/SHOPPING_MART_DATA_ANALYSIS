import time
start = time.time()

print('Hello world')
print('today is thursday')
print(type('a'))
print(type(1))
print(type(123j))

a=b=c=5
a,b,c = 1,'sddfdsf',2
print(a,b,c)

a=2
b=5
print("({} + {})^2 = {}^2 + 2*{}*{} +{}^2".format(a,b,a,a,b,b))

if 2>3:
    pass

myname = 'abhijith mallya'
if 'abhi' in myname : 
    print('true')

a=10
b=20
print("True Block") if a<b else print("False Block")

end = time.time()
print("End time ({}) - Start time ({}) = {} seconds".format(round(end,3),round(start,3),round((end-start),2)))

