#!/usr/bin/env python

"""
An example of using logger-py.

A box is showing growing and shrinking, and visualization
data is printed to STDOUT.

Running:
./morphing_box.py 1> morphing_box.json

Visualizing:
Drag morphing_box.json onto the window: https://review.github.io/
"""

# Kludge to import logger from a relative path
from sys import path, stderr

path.append("../logger")
from logger import Logger

BOX_NAME = "box"
BOX_SIZE = [0.25, 0.5, 0.1]
BOX_COLOR = [1, 1, 0, 1]
BOX_POS = [0, BOX_SIZE[1] / 2, 0]
BOX_ROT = [0, 0, 0, 1]

VISUALIZATION_STEP = 1


def morphing_box():
    """A simple example of changing the shape of an object."""

    # Create the logger
    logger = Logger("Morphing Box", VISUALIZATION_STEP)

    # Add all objects
    logger.add_box(BOX_NAME, *BOX_SIZE, BOX_COLOR)

    # Add box initial position
    logger.add_frame(BOX_NAME, BOX_POS, BOX_ROT, BOX_SIZE)

    # Change scale of box and add new frame
    new_size = BOX_SIZE.copy()
    new_size[1] *= 5

    new_pos = BOX_POS.copy()
    new_pos[1] *= 5

    logger.add_frame(BOX_NAME, new_pos, BOX_ROT, new_size)

    # Change scale of box and add new frame again
    new_size = new_size.copy()
    new_size[0] *= 2
    logger.add_frame(BOX_NAME, new_pos, BOX_ROT, new_size)

    # Add a delay by inserting empty frames
    logger.new_frame()

    # Change scale of box and add new frame again
    new_size = new_size.copy()
    new_size[0] *= 3
    new_size[1] *= 0.1
    new_size[2] *= 10
    new_pos = new_pos.copy()
    new_pos[1] *= 0.1
    logger.add_frame(BOX_NAME, new_pos, BOX_ROT, new_size)

    # Add a delay by inserting empty frames
    logger.new_frame()
    logger.new_frame()

    # Print visualization data
    print(str(logger))


if __name__ == "__main__":
    morphing_box()
