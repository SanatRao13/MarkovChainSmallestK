# MarkovChainSmallestK
Calculates the smallest k iterations necessary for the k-th iteration to match the steady-state distribution to a certain decimal point
The user must specify how many decimal places to consider in the comparison (typically less than 10)
The user must also type their transformation matrix and initial distribution matrix as numpy arrays (detailed in code)
The power on the transformation matrix to mimic the infinite-iterations matrix can be adjusted based on user preferences
Then the program finds the minimum number of transformations necessary (k) for the distribution after k iterations to be similar to the steady state solution to n decimal places
