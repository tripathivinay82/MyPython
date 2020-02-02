# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:01:27 2020

@author: vinayt
"""

def board_draw(height, width):
    top = "┌" + "┬".join(["─"*6]*width) + "┐\n"
    bottom = "└" + "┴".join(["─"*6]*width) + "┘"
    middle = "├" + "┼".join(["─"*6]*width) + "┤\n"
    print(top +
          middle.join(
              "│" +
              "│".join('  {:02d}  '.format(x * width + y + 1)
                       for y in range(width)) +
              "│\n"
              for x in range(height)) +
          bottom)

board_draw(3,3)