import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self): return self.x
    def get_y(self): return self.y
    def set_x(self, x): self.x = x
    def set_y(self, y): self.y = y

    def print_point(self):
        print('('+str(self.x)+', '+str(self.y)+')')

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.type_line = True #прямая имеет вид y = k*x + b
        #False если прямая имеет вид x = a
        try:
            self.k = (p1.get_y()-p2.get_y())/(p1.get_x()-p2.get_x())
            self.b = p1.get_y() - self.k * p1.get_x()
        except ZeroDivisionError:
            self.a = p1.get_x()
            self.type_line = False
    def print_line(self):
        if self.type_line:
            print('y = '+ str(self.k)+'x + '+ str(self.b))
            self.p1.print_point()
            self.p2.print_point()
        else:
            print('x = ' + str(self.a))

    def is_intersect(self, other): #проверка пересения двух отрезков
        if self.type_line:
            a1 = [1, -self.k]
            b1 = self.b
        else:
            a1 = [0, 1]
            b1 = self.a
        if other.type_line:
            a2 = [1, -other.k]
            b2 = other.b
        else:
            a2 = [0, 1]
            b2 = other.a

        a = np.array([a1, a2])
        b = np.array([b1, b2])

        try:
            x = np.linalg.solve(a, b)
            if self.p1.get_x() <= x[1] <= self.p2.get_x() and self.p1.get_y() <= x[0] <= self.p2.get_y() and other.p1.get_x() <= x[1] <= other.p2.get_x() and other.p1.get_y() <= x[0] <= other.p2.get_y():
                return True
            else:
                return False

        except np.linalg.LinAlgError:
            return False

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.l12 = Line(p1, p2)
        self.l13 = Line(p1, p3)
        self.l23 = Line(p2, p3)

    def get_l12(self): return self.l12
    def get_l13(self): return self.l13
    def get_l23(self): return self.l23

    def move(self, dx, dy):
        self.p1.set_x(self.p1.get_x() + dx)
        self.p2.set_x(self.p2.get_x() + dx)
        self.p3.set_x(self.p3.get_x() + dx)

        self.p1.set_y(self.p1.get_y() + dy)
        self.p2.set_y(self.p2.get_y() + dy)
        self.p3.set_y(self.p3.get_y() + dy)

        self.l12 = Line(self.p1, self.p2)
        self.l13 = Line(self.p1, self.p3)
        self.l23 = Line(self.p2, self.p3)

    def print_triangle(self):
        self.p1.print_point()
        self.p2.print_point()
        self.p3.print_point()

class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.l12 = Line(p1, p2)
        self.l14 = Line(p1, p4)
        self.l23 = Line(p2, p3)
        self.l34 = Line(p3, p4)

    def move(self, dx, dy):
        self.p1.set_x(self.p1.get_x() + dx)
        self.p2.set_x(self.p2.get_x() + dx)
        self.p3.set_x(self.p3.get_x() + dx)
        self.p4.set_x(self.p4.get_x() + dx)

        self.p1.set_y(self.p1.get_y() + dy)
        self.p2.set_y(self.p2.get_y() + dy)
        self.p3.set_y(self.p3.get_y() + dy)
        self.p4.set_y(self.p4.get_y() + dy)

        self.l12 = Line(self.p1, self.p2)
        self.l13 = Line(self.p1, self.p3)
        self.l14 = Line(self.p1, self.p4)
        self.l23 = Line(self.p2, self.p3)
        self.l24 = Line(self.p2, self.p4)
        self.l34 = Line(self.p3, self.p4)

    def is_intersect(self, tr):
        l_r = [self.l12, self.l14, self.l23, self.l34]
        l_tr = [tr.get_l12(), tr.get_l13(), tr.get_l23()]
        b = False
        for x in l_r:
            for y in l_tr:
                if x.is_intersect(y):
                    b = True
        return b

print('Введите координаты точек треугольника:')
tr_p = []
for i in range(3):
    x = float(input('x = '))
    y = float(input('y = '))
    tr_p.append(Point(x, y))
tr = Triangle(tr_p[0], tr_p[1], tr_p[2])

print('Введите координаты точек четырехугольника:')
rect_p = []
for i in range(4):
    x = float(input('x = '))
    y = float(input('y = '))
    rect_p.append(Point(x, y))
rect = Rectangle(rect_p[0], rect_p[1],rect_p[2],rect_p[3])

if rect.is_intersect(tr):
    print('Треугольник и прямоугольник пересекаются')
else:
    print('Треугольник и прямоугольник не пересекаются')

print('Введите свдиг точек точек треугольника:')
dx = float(input('dx = '))
dy = float(input('dy = '))

tr.move(dx, dy)
tr.print_triangle()