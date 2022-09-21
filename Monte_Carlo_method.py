import numpy
from manim import *
from math import pi


class MonteCarlo(Scene):
    def construct(self):
        num = 0
        myplane = (
            NumberPlane(
                x_range=[0, 500, 50], x_length=5, y_range=[0, 5, 0.5], y_length=5
            )
            .shift(DOWN + 2 * RIGHT)
            .add_coordinates()
        )
        self.add(myplane)
        line = myplane.get_horizontal_line(myplane.c2p(510, pi, 0), color=YELLOW)
        self.add(line)
        circle = Circle(radius=1, color=GREEN).shift(UP + 2 * LEFT)
        square = Square(side_length=2, color=RED).shift(UP + 2 * LEFT)
        self.play(DrawBorderThenFill(myplane))
        self.play(Create(circle))
        self.play(Create(square))
        dot_group = VGroup()
        self.add(dot_group)
        num = 50
        sub_num = 0
        eq1 = MathTex(r"\pi").shift(3 * UP + 7 * LEFT)
        self.add(eq1)
        self.play(FadeIn(eq1))
        eq2 = MathTex(r"=4*\frac{Area \ of \ Circle}{Area \ of \ Square}").next_to(
            eq1, 2 * RIGHT
        )
        self.add(eq2)
        self.play(FadeIn(eq2))
        eq3 = MathTex(
            r"=4*\frac{Number \ of \ point \ in \ Circle}{Number \ of \ points \ in \ square}"
        ).next_to(eq2, 2 * RIGHT)
        self.play(FadeIn(eq3))
        pi_current = 0
        pi_previous = 0
        while num != 550:
            dot_subgroup = VGroup()
            for i in range(50):
                a, b = (
                    numpy.random.uniform(-1, 1, 1)[0],
                    numpy.random.uniform(-1, 1, 1)[0],
                )
                dot = Dot(point=(a, b, 0)).shift(UP + 2 * LEFT)
                if a**2 + b**2 <= 1:
                    sub_num += 1
                dot_subgroup.add(dot)
            dot_group.add(dot_subgroup)
            self.play(FadeIn(dot_subgroup))
            pi_current = 4 * sub_num / num
            
            line=Line(
                    start=myplane.c2p(num-50,pi_previous,0),
                    end=myplane.c2p(num, pi_current, 0), color=GREEN
                )
            dot=Dot(point=myplane.c2p(num,pi_current,0),color=BLUE)
            label=MathTex(r"("+str(num)+", "+str(pi_current)[:4]+")").scale(0.4).next_to(dot,UP if (num//50)%2==1 else DOWN)
            self.add(line)
            self.play(Create(line))
            self.add(dot)
            self.play(FadeIn(dot))
            self.add(label)
            self.play(Write(label))
            pi_previous = pi_current
            self.wait(2)
            num += 50
