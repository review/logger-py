#!/usr/bin/env python

"""
An example of using logger-py.

Two bouncing sphere are simulated and visualization data
is printed to STDOUT.

I typically print visualization data to STDOUT, and
logging data to STDERR.

Running:
./falling_sphere.py 1> falling_sphere.json 2> falling_sphere.csv

Plotting (https://github.com/anthonyjclark/scripts/blob/master/piplot.py):
piplot.py -f falling_sphere.csv -x t

Visualizing:
Drag falling_sphere.json onto the window: https://review.github.io/
"""

# Kludge to import logger from a relative path
from sys import path, stderr
path.append('../logger')
from logger import Logger

OBJS = [
    {
        "name": "red-ball",
        "radius": 0.25,
        "restitution": 0.85,
        "color": [1, 0, 0, 1],
        "pos": [-1, 4, 0],
        "rot": [0, 0, 0, 1],
        "vel": [0, 0, 0, 0, 0, 0],
    }, {
        "name": "blue-ball",
        "radius": 0.5,
        "restitution": 0.95,
        "color": [0, 0, 1, 1],
        "pos": [1, 4, 0],
        "rot": [0, 0, 0, 1],
        "vel": [0, 0, 0, 0, 0, 0],
    }
]

TIME_STOP_MS = 8*1000

SIMULATION_STEP_MS = 50
SIMULATION_STEP = SIMULATION_STEP_MS/1000
VISUALIZATION_STEP_MS = 100

GRAVITY = -9.81
X, Y, Z = 0, 1, 2


def bouncing_ball_simulation():
    """Simulate two bouncing spheres."""

    # Create the logger
    logger = Logger(VISUALIZATION_STEP_MS/1000)

    # Add all objects
    for obj in OBJS:
        logger.add_sphere(obj["name"], obj["radius"], obj["color"])

    # Create the initial frame
    logger.new_frame()
    for obj in OBJS:
        # Must pass a copy of position and rotation
        # since python passes by reference.
        pos, rot = obj["pos"].copy(), obj["rot"].copy()
        logger.add_to_frame(obj["name"], pos, rot)

    time_ms = 0
    next_vis_update_ms = VISUALIZATION_STEP_MS

    print("t,red-ball position, blue-ball position", file=stderr)
    print(f"0,{OBJS[0]['pos'][Y]},{OBJS[1]['pos'][Y]}", file=stderr)

    while time_ms <= TIME_STOP_MS:
        time_ms += SIMULATION_STEP_MS

        # Physics calculation
        for obj in OBJS:
            obj["pos"][Y] += obj["vel"][Y]*SIMULATION_STEP
            obj["vel"][Y] += GRAVITY*SIMULATION_STEP

        # Check for bouncing
        for obj in OBJS:
            penetration_dist = obj["pos"][Y] - obj["radius"]
            if penetration_dist <= 0:
                obj["pos"][Y] = -penetration_dist
                obj["vel"][Y] *= -1*obj["restitution"]

        # Update the visualization
        if time_ms >= next_vis_update_ms:
            next_vis_update_ms += VISUALIZATION_STEP_MS

            # Print to STDERR for logging separately from json data
            print(f"{time_ms/1000},{OBJS[0]['pos'][Y]},{OBJS[1]['pos'][Y]}",
                  file=stderr)

            logger.new_frame()
            for obj in OBJS:
                pos, rot = obj["pos"].copy(), obj["rot"].copy()
                logger.add_to_frame(obj["name"], pos, rot)

    print(str(logger))


if __name__ == '__main__':
    bouncing_ball_simulation()
