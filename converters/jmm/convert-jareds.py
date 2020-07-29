#!/usr/bin/env python3

import json
import sys


animation_filename = sys.argv[1]
with open(animation_filename, 'r') as animation_file:
    animation_data = animation_file.readlines()

json_data = {}

json_data['timeStep'] = float(animation_data[2])
json_data['name'] = "Jared's Animation"

num_box = int(sys.argv[2])
num_cap = int(sys.argv[3])
dat_start = int(sys.argv[4])

# Setup objects
colors = [[1.000, 0.766, 0.336, 1.0]] * num_box \
       + [[0.080, 0.700, 0.600, 1.0]] * 4 \
       + [[0.700, 0.150, 0.150, 1.0]] * 4 \
       + [[0.150, 0.150, 0.700, 1.0]] * 4
names = []
json_data['objects'] = []
for i, primitive in enumerate(animation_data[4:4+num_box+num_cap]):

    primitive = primitive.split(',')

    if primitive[0] == 'box':
        obj_mesh = 'cube'
        obj_scale = [float(v) for v in primitive[4:7]]
    else:
        obj_mesh = 'cylinder'
        radius = float(primitive[5])
        height = float(primitive[4])
        obj_scale = [radius, height, radius]

    obj_name = obj_mesh + str(i)
    names.append(obj_name)

    json_data['objects'].append({
        'name': obj_name,
        'mesh': obj_mesh,
        'scale': obj_scale,
        'material': { 'color': colors[i] },
    })

# Setup frames
json_data['frames'] = []
for pos, rot in zip(animation_data[dat_start::2], animation_data[dat_start+1::2]):

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
