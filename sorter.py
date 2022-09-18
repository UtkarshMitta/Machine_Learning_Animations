from manim import *
import numpy


def create_textbox(color, string):
    result = VGroup()
    box = Rectangle(
        height=1, width=1, fill_color=color, fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center())
    result.add(box, text)
    return result


arrow_i = Arrow(start=UP, end=DOWN, color=BLUE)
arrow_j = Arrow(start=UP, end=DOWN, color=GREEN)


textboxlist = []


def make_textbox_system(numpy_array, textbox_list, self):
    for i in range(len(numpy_array)):
        a = str(numpy_array[i])
        textbox = create_textbox(color=GREEN, string=a[0 : len(a) - 2])
        textbox_list.append(textbox)
        self.add(textbox_list[i])
    textboxlist[0].shift(5 * LEFT)
    for i in range(1, len(textbox_list), 1):
        textbox_list[i].next_to(textbox_list[i - 1], 2 * RIGHT)
    arrow_i.next_to(textbox_list[0], 2 * UP)
    arrow_j.next_to(textbox_list[1], 2 * UP)


def swap(numpy_array, textbox_list, i, j, self):
    numpy_array[i], numpy_array[j] = numpy_array[j], numpy_array[i]
    self.play(CyclicReplace(textbox_list[i], textbox_list[j]))
    textbox_list[i], textbox_list[j] = textbox_list[j], textbox_list[i]
