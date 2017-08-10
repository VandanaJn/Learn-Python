"""This module explores basic python language constructs."""
def hello(name):
    print "Hello " + name

hello("John")

def add(x,y):
    return x+y
print add(6,5)

def int_formats(num):
    print ('{:d} '+'{:d}'.format(num))
    print ('{: d} '+'{: d}'.format(num))
    print ('{:+d} '+'{:+d}'.format(num))
    print ('{:2d} '+'{:2d}'.format(num))
    print ('{:5d} '+'{:5d}'.format(num)) #padding

int_formats(1234)
int_formats(-1234)

def float_formats(num):
    print ('{:f} '+'{:f}'.format(num))
    print ('{:5.3f} '+'{:5.3f}'.format(num)) #no padding,  rounds
    print ('{:6.4f} '+'{:6.4f}'.format(num)) #no padding,  rounds 

float_formats(1345.344555)