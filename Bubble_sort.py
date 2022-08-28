from manim import *


def create_textbox(color, string):
    result = VGroup()
    box = Rectangle(
        height=1, width=1, fill_color=color, fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result


class TextBox(Scene):
    def construct(self):
        textboxlist = []
        l = []
        n = int(input())
        for i in range(n):
            a = input()
            l.append(int(a))
            textboxlist.append(create_textbox(color=GREEN, string=a))
        textboxlist[0].shift(5 * LEFT)
        arrow1 = Arrow(start=UP, end=DOWN, color=BLUE)
        arrow2 = Arrow(start=UP, end=DOWN, color=GREEN)
        for i in range(len(l) - 1):
            textboxlist[i + 1].next_to(textboxlist[i], 2 * RIGHT)
        self.add(arrow1, arrow2)
        for textbox in textboxlist:
            self.add(textbox)
        for i in range(len(l) - 1):
            for j in range(len(l) - i - 1):
                arrow1.next_to(textboxlist[j], 2 * UP)
                arrow2.next_to(textboxlist[j + 1], 2 * UP)
                animations = [
                    FadeIn(arrow1.next_to(textboxlist[j], 2 * UP)),
                    FadeIn(arrow2.next_to(textboxlist[j + 1], 2 * UP)),
                ]
                self.play(AnimationGroup(*animations))
                animations = [FadeOut(arrow1), FadeOut(arrow2)]
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
                    self.play(CyclicReplace(textboxlist[j], textboxlist[j + 1]))
                    self.play(AnimationGroup(*animations))
                    textboxlist[j], textboxlist[j + 1] = (
                        textboxlist[j + 1],
                        textboxlist[j],
                    )
                self.wait(1)
