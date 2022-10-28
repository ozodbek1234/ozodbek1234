# import numpy as np
# import matplotlib.pyplot as plt
# y=lambda x:x**2+2*x+1
# y1=lambda x:x
# x = np.linspace(-3, 3,100)

# fig=plt.subplots()
# plt.plot(x, y(x))
# plt.plot(x, y1(x))
# plt.show()
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
# уравнение поверхности
f = lambda x, y: x ** 2 - y ** 2
# создаём полотно для рисунка
fig = plt.figure(figsize = (10, 10))
# создаём рисунок пространства с поверхностью
ax = fig.add_subplot(1, 1, 1, projection = '3d')
# размечаем границы осей для аргументов
xval = np.linspace(-4, 4, 100)
yval = np.linspace(-4, 4, 100)
# создаём массив с xval столбцами и yval строками
# - в этом массиве будут храниться значения z
x, y = np.meshgrid(xval, yval)
# приравниваем z к функции от x и y 
z = f(x, y)
# создаём поверхность
surf = ax.plot_surface(
# отмечаем аргументы и уравнение поверхности
x, y, z, 
# шаг прорисовки сетки
# - чем меньше значение, тем плавнее
# - будет градиент на поверхности
rstride = 10,
cstride = 10,
# цветовая схема plasma
cmap = cm.plasma)