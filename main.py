<<<<<<< HEAD

x = 15
print(bin(x)[2:])
=======
import matplotlib.pyplot as plt
# Создание объекта Figure
fig = plt.figure()
# тип объекта Figure
print (type(fig))
# scatter - метод для нанесения маркера в точке (1.0, 1.0)
for i in range(1,10):
    plt.scatter(i,i)
print (fig.axes)
# После нанесения графического элемента в виде маркера, список текущих областей состоит из одной области
plt.show()
>>>>>>> daf6169def027df1b2e6ce219de56e18089e3469
