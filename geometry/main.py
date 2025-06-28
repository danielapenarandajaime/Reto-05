import math

from base.shape import Shape, Line, Point

from formas.rectangle import Rectangle, Square

from formas.triangle import Triangle, TriRectangle, Equilateral, Scalene, Isosceles



if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 2)
    p4 = Point(0, 2)

    rect = Rectangle([p1, p2, p3, p4])
    print("Área del rectángulo:", rect.compute_area())  # 8 
    print("Perímetro del rectángulo:", rect.compute_perimeter())  # 12 
    print("Ángulos internos:", rect.compute_inner_angles())  

    p_test1 = Point(2, 1)
    p_test2 = Point(5, 3)
    print(rect.compute_interference_point(p_test1))  # Inside
    print(rect.compute_interference_point(p_test2))  # Outside

    p10 = Point(0, 0)
    p20 = Point(2, 0)
    p30 = Point(2, 2)
    p40 = Point(0, 2)

    square = Square([p10, p20, p30, p40], None)
    print("Área del cuadrado:", square.compute_area())  # 4
    print("Perímetro del cuadrado:", square.compute_perimeter())  # 8

    p11 = Point(0, 0)
    p21 = Point(3, 0)
    p31 = Point(1.5, 2.6)

    triangle = Triangle([p11, p21, p31], None)
    print("Área del triángulo:", triangle.compute_area())
    print("Perímetro del triángulo:", triangle.compute_perimeter())
    print("Ángulos internos:", triangle.compute_inner_angles())

    p12 = Point(0, 0)
    p22 = Point(2, 0)
    p32 = Point(1, 2)

    isosceles = Isosceles([p12, p22, p32], None)
    print("Es isósceles válido?", isosceles._is_regular)  # False 

    p13 = Point(0, 0)
    p23 = Point(2, 0)
    p33 = Point(1, math.sqrt(3))

    equilateral = Equilateral([p13, p23, p33], None)
    print("Es equilátero válido?", equilateral._is_regular)  # True

    p14 = Point(0, 0)
    p24 = Point(3, 0)
    p34 = Point(1, 2)

    scalene = Scalene([p14, p24, p34], None)
    print("Es escaleno válido?", scalene._is_regular)  # True

    p15 = Point(0, 0)
    p25 = Point(3, 0)
    p35 = Point(0, 4)

    tri_rect = TriRectangle([p15, p25, p35], None)
    print("Área del triángulo rectángulo:", tri_rect.compute_area())  # 6 
    print("Es triángulo rectángulo válido?", 90 in tri_rect.compute_inner_angles())  # True
