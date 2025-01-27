def func(num1, num2):
    print(num1 + num2)
    #return num1 + num2
func(3, 5)
func('hello ', 'all')
func([1,2,3], [4,5,6]) 

#----------------------------#

def arguments(*args):
    print(args)
    for arg in args:
        print(arg)
arguments(1,2,3,4,"Any", "thing")

#----------------------------#

def keyword(**kywords):
    print(kywords)
    for keyword in kywords:
        print(kywords[keyword])
keyword(model = "Toyota", year = 2015 )