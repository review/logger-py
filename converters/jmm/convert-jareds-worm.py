#!/usr/bin/env python3

import json
import sys


animation_filename = sys.argv[1]

num_boxes = int(sys.argv[2])

with open(animation_filename, 'r') as animation_file:
    animation_data = animation_file.readlines()

json_data = {}

json_data['timeStep'] = float(animation_data[2])
json_data['name'] = "Jared's Animation"

# Setup objects
color = [1.0, 0.4, 0.3, 1.0]
names = []
json_data['objects'] = []
for i, primitive in enumerate(animation_data[4:4+num_boxes]):

    primitive = primitive.split(',')

    obj_mesh = 'cube'
    obj_scale = [float(v) for v in primitive[4:7]]
    obj_name = obj_mesh + str(i)

    names.append(obj_name)

    json_data['objects'].append({
        'name': obj_name,
        'mesh': obj_mesh,
        'scale': obj_scale,
        'material': { 'color': color },
    })

# Setup frames
json_data['frames'] = []
for pos, rot in zip(animation_data[4+num_boxes+1::2], animation_data[4+num_boxes+2::2]):

    frame = {}
    for i, name in enumerate(names):

        obj_t = [float(v) for v in pos.split(',')[i*3:i*3+3]]
        obj_r = [float(v) for v in rot.split(',')[i*4:i*4+4]]
        obj_r = [obj_r[1], obj_r[2], obj_r[3], obj_r[0]]

        frame[name] = {
            't': obj_t,
            'r': obj_r
        }

    json_data['frames'].append(frame)

json_data['timeStep'] = json_data['duration'] / (len(json_data['frames']) - 1)

print(json.dumps(json_data, indent=2, separators=(',', ': ')))
