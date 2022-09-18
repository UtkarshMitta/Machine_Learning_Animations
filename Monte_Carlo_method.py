import numpy
from manim import *
from math import pi


class MonteCarlo(Scene):
    def construct(self):
        n = int(input())
        circle = Circle(radius=1, color=GREEN)
        square = Square(side_length=2, color=RED)
        self.add(circle)
        self.play(Create(circle))
        self.play(Create(square))
        x_coor = numpy.random.uniform(-1, 1, n)
        y_coor = numpy.random.uniform(-1, 1, n)
        combinations = numpy.array([(i, j) for i in x_coor for j in y_coor])
        num=0
        dot_group = VGroup()
        for coordinates in combinations:
            dot = Dot(point=numpy.array([coordinates[0], coordinates[1], 0]))
            dot_group += dot
            self.add(dot)
            if coordinates[0] ** 2 + coordinates[1] ** 2 <= 1:
                num+=1
        eq1 = MathTex(r"\frac{\pi}{4}").shift(3*UP+7*LEFT)
        self.add(eq1)
        self.play(FadeIn(eq1))
        eq2=MathTex(r"=\frac{Area \ of \ Circle}{Area \ of \ Square}").next_to(eq1,2*RIGHT)
        self.add(eq2)
        self.play(FadeIn(eq2))
        eq3=MathTex(r"=\frac{Number \ of \ point \ in \ Circle}{Number \ of \ points \ in \ square}").next_to(eq2,2*RIGHT)
        self.play(FadeIn(eq3))
        eq4=MathTex(r"="+str(num/n**2)).next_to(eq3,2*RIGHT)
        self.add(eq4)
        self.play(FadeIn(eq4))

