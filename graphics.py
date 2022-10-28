import matplotlib.pyplot as pyplot
x=[]
y=[]
i=-10
while i<10:
    
    x.append(i)
    y.append(i*i+2*i+1)
    i+=0.01
    
pyplot.plot(x,y)#
pyplot.xlabel('x')#
pyplot.ylabel('y')
pyplot.title('kvadrat funksiya')
pyplot.show()
