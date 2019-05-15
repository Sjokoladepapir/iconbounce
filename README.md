# iconbounce

As of now, running NaivePathAlgorithm.py produces a demo. The integers rows and columns can be tweaked to get
different demo results.

This project was built as a python implimentation of what happens if one selects a random icon on the desktop,
chooses to only be able to move only diagonally, bounce and change direction when an edge is reached, and stops
when a corner is reached. This creates a path, which could be circular, or have a beginning and an end.

worldBouilderTest contains the class Rectangle, which creates an object containing the icon space in the form of
an 2d array. Ones represent icons, zeroes (or being outside of the range of the matrix) represent the absence of them.

This array is then used to generate two arrays, in "Cross space". Here instead of keeping track of where the icons are,
the arrays keeps track of the type of connections and direction of the them instead. As of now this happens in
NaivecrossStateSpace.py, which imports naiveRules.py. naiveRules is used togther with NaivecrossStateSpace.py
to check which type of connection should be used.

naivePathAlgorithm.py then takes these two arrays and creates two new arrays,
each of them keeps track of path and direction of the path.

This is then plotted with matplotlib.