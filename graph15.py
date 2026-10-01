import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0., 5., 0.2)
lines = plt.plot(t, t, 'b-', t, t**2, 'r-',t, t**3, 'g-', linewidth=2.0)
plt.setp(lines, color='r', linewidth=2.0)
plt.xlabel('Dummy data for x')
plt.ylabel('Dummy data for y')
plt.title('An example graph')
plt.text(1, 80, 'lew is good at graphs')
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
plt.savefig('test.png')
plt.show()
