import math
import csv

PI = math.pi

def give_dots(R,r,r_,resolution=2*PI/1000,spins=5):

    def x(theta):
        x =  (R - r) * math.cos( theta ) + r_* math.cos( (R - r) / r * theta )
        return x

    def y(theta):
        y =  (R - r) * math.sin( theta ) - r_* math.sin( (R - r) / r * theta )
        return y

    theta = 0.0
    while theta < 2*PI*spins:
        out.write('{},{} \n'.format(x(theta), y(theta)))

        yield (x(theta), y(theta))
        theta += resolution


if __name__=='__main__':

    from pylab import *

    input_name = input("Name?: ")
    out = open ('../results/cartesian_results/' + 'spiro' + input_name + '.csv', 'w')

    dots = give_dots(4,10,5.5, spins=25)

    x,y = zip(*dots)


    plot(x,y)

    show()
