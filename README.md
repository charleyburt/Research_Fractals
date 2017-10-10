# Research Fractals

Summary
------

This goal of this project is to determine how the "width" of a fractal changes
relative to it's circumference. Much is known about how the circumference of fractals change over 
each iteration. For instance, the `Koch Curve` 
[will actually diverge to infinity](https://www.cut-the-knot.org/WhatIs/Infinity/Length-Area.shtml)
. However, not much is known about the "width" of fractals. Mostly because, in my opinion, an accurate
definition of width does not exist for convex bodies. So, after looking at several existing definitions 
for width, my advisor [Prof. Kris Williams](http://www.doane.edu/kristopher-williams), and I came 
up with our own. The following walks through the basics of it. 


Quick Start
------

`./Different_Shapes/*`
  - Allows the user to choose the number of iterations
  - Draws the Shape
  - Saves the "corner" points to a file
  - Prints out the circumference

`./Data_Process/`
- `Filler.py`
  - Reads in the file exported by `Koch_Snowflake.py`
  - Creates a certain number of points (specified by user) between the "corners"
  - Exports a new file with "filled in" lines 
  
- `Polar_Colverter.py`
  - Reads in the file exported by `Filler.py`
  - Converts (x,y) coordiantes to (r, theta)

- `Width_Finder.py`
  - Reads in a file exported by `Polar_Converter.py`
  - Goes through the file and finds the largest `r` for each `theta` specified by the user
	- For examples there may be multiple points at a given `theta`. This will only find the furthest point from the origin.
	- Every degree would give 360 samples, 0.5 angles would give 720 samples, etc.
  - Returns the average "width" of a fractal 

Credits
------

This repo is developed and maintained by Charley Burtwistle under the guidance of Professor Kris Williams.
Any questions or comments can be sent to charley.burtwistle@doane.edu .

