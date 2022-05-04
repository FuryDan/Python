print('\n test 1 \n')
import numpy as np

t = np.array([[1,2],[3,4]])
print(t)
print('\n test 1 finished succesfully')


print('\n test 2 \n')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
print('\n test 2 finished succesfully')


print('\n test 3 \n')
import matplotlib.pyplot as plt

fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title("Fruits for sale")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()
print('\n test 3 finished succesfully')


print('\n test 4 \n')

print('\n test 4 finished succesfully')