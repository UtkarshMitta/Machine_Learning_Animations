from manim import *
import sorter
import numpy


class TextBox(Scene):
    def construct(self):
        n = int(input())
        arr = numpy.zeros(n)
        for i in range(n):
            arr[i] = int(input())
        sorter.make_textbox_system(arr, sorter.textboxlist, self)
        for i in range(n):
            for j in range(n - i - 1):
                sorter.arrow_i.next_to(sorter.textboxlist[j], 2 * UP)
                sorter.arrow_j.next_to(sorter.textboxlist[j + 1], 2 * UP)
                animations = [
                    FadeIn(sorter.arrow_i.next_to(sorter.textboxlist[j], 2 * UP)),
                    FadeIn(sorter.arrow_j.next_to(sorter.textboxlist[j + 1], 2 * UP)),
                ]
                self.play(AnimationGroup(*animations))
                if arr[j + 1] < arr[j]:
                    sorter.swap(arr, sorter.textboxlist, j + 1, j, self)
                animations = [
                    FadeOut(sorter.arrow_i.next_to(sorter.textboxlist[j], 2 * UP)),
                    FadeOut(sorter.arrow_j.next_to(sorter.textboxlist[j + 1], 2 * UP)),
                ]
                self.play(AnimationGroup(*animations))
                self.wait(1)
