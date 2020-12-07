import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
data = norm.rvs(10.0, 2.5, size=500) # Δημιουργία δεδομένων
mu, std = norm.fit(data) # Μοντελοποίηση με μια κανονική κατανομή
plt.hist(data, bins=25, density=True, alpha=0.3, color='g')
xmin, xmax = plt.xlim() # όρια του άξονα x
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.show()