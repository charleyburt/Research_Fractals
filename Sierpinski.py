from turtle import *



def Side(l,d):
  if(d==0):
     forward(l)
     return

  Side(l/2, d-1)
  diagUp(l/2)
  Side(l/2,d-1)
  diagDown(l/2)
  Side(l/2,d-1)


def diagUp(l):

   left(120)
   forward(l)
   right(120)


def diagDown(l):
   right(120)
   forward(l)
   left(120)

if __name__ == "__main__":
      speed('fastest')
      depth = 5
      size  = 300
      Side(size,depth)
      right(120)
      Side(size,depth)
      right(120)
      Side(size,depth)
      done()
