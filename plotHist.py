# plot an histogram of binomial distributed numbers

import numpy
import matplotlib.pyplot as plt

randNumbers = numpy.random.binomial(1000, .75, 5000)

plt.hist(randNumbers,100)
plt.title("Histogram of randomly choosen binomial numbers")
plt.xlabel("range")
plt.show()