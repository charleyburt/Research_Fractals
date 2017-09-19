# Research Fractals

Quick Start
------

`Koch_Snowflake.py`
  - Allows the user to choose the number of iterations
  - Draws the Snowflake
  - Saves the "corner" points to a file
  - Prints out the circumference

`Filler.py`
  - Reads in the file exported by `Koch_Snowflake.py`
  - Creates a certain number of points (specified by user) between the "corners"
  - Exports a new file with "filled in" lines 
  
`Polar_Colverter.py`
  - Reads in the file exported by `Filler.py`
  - Converts (x,y) coordiantes to (r, theta)

`Width_Finder.py` **DEV**
  - Reads in a file exported by `Polar_Converter.py`
  - Goes through the file and finds the largest `theta` for each `r` specified by the user
