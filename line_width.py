from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from sympy import pprint

def LineWidth():

    a, k, h = symbols('a, k, h', real=True)

    ax=3
    ay=5
    bx=1
    by=-1

    eq1 = a*(ax-k)**2 +a*(ay-h)**2 - 1
    eq2 = a*(bx-k)**2 +a*(by-h)**2 - 1
    eq3 = ax/ay*(-a*(ax-k)/(a*(ay-h)))-1

    system = [eq1,eq2,eq3]

    solution=nonlinsolve(system,[a,k,h])

    pprint(solution)

    # A=line([(0,0), (ax,ay)])
    # aa=point
    # B=line([(0,0), (bx,by)])
    # C=implicit_plot( q[0][0].rhs()*(x-q[0][2].rhs())^2 + q[0][0].rhs()*(y-q[0][3].rhs())^2 -1, (x,-5,5), (y,-5,5))
    # show(A+B+C)

if __name__ == "__main__":
    LineWidth()
