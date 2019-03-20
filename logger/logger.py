"""
The logger.py module is used to produce logged output in the
Review format. For more information see:
https://github.com/review/
"""

import json

DEFAULT_COLOR = (1, 1, 1, 1)


class Logger(object):
    """A logger for review.github.io"""

    def __init__(self, vis_step, name=None):
        """Create a new logger instance.

        vis_step : time step between logged frame data
        name     : an optional name for the logged data
        """
        super(Logger, self).__init__()

        self.log_data = {"objects": [], "frames": []}
        self.positions = {}

        if name is not None:
            self.log_data["name"] = name

        self.log_data["timeStep"] = vis_step

    def add_object(self, name, obj_type, scale, color):
        """Utility method called by add_*."""

        self.log_data["objects"].append({
            "name": name,
            "mesh": obj_type,
            "scale": scale,
            "material": {"color": color}
        })

    def add_sphere(self, name, radius, color=DEFAULT_COLOR):
        """Add a sphere to the logged data.

        This should be called at the beginning of your
        simulation/animation (it needs to be called before new_frame,
        add_to_frame, and add_frame).

        name   : name of the object
        radius : radius of the sphere
        color  : color of the object (defaults to white)
        """
        self.add_object(name, "sphere", (radius, radius, radius), color)

    def add_ellipsoid(self, name, xsize, ysize, zsize, color=DEFAULT_COLOR):
        """Add an ellipsoid to the logged data.

        This should be called at the beginning of your
        simulation/animation (it needs to be called before new_frame,
        add_to_frame, and add_frame).

        name   : name of the object
        xsize : size in the x direction for the sphere
        ysize : size in the y direction for the sphere
        zsize : size in the z direction for the sphere
        color  : color of the object (defaults to white)
        """
        # Dividing by 2 because review expects radius values
        self.add_object(name, "sphere", (xsize/2, ysize/2, zsize/2), color)

    def add_box(self, name, xsize, ysize, zsize, color=DEFAULT_COLOR):
        """Add a box (cuboid) to the logged data.

        This should be called at the beginning of your
        simulation/animation (it needs to be called before new_frame,
        add_to_frame, and add_frame).

        name   : name of the object
        xsize : size in the x direction for the sphere
        ysize : size in the y direction for the sphere
        zsize : size in the z direction for the sphere
        color  : color of the object (defaults to white)
        """
        self.add_object(name, "cube", (xsize, ysize, zsize), color)

    def add_cylinder(self, name, radius, height, color=DEFAULT_COLOR):
        """Add a cylinder to the logged data.

        This should be called at the beginning of your
        simulation/animation (it needs to be called before new_frame,
        add_to_frame, and add_frame).

        name   : name of the object
        radius : radius of the cylinder
        height : height of the cylinder
        color  : color of the object (defaults to white)
        """
        self.add_object(name, "cylinder", (radius, height, radius), color)

    def new_frame(self):
        """Add a new frame for the current time step.

        This function should be called before add_to_frame.
        """
        self.log_data["frames"].append({})

    def enough_motion(self, name, pos, quat, t_tol=0.01, r_tol=0.01):
        """Return true if object has moved more than tolerance."""
        return name not in self.positions or \
               abs(pos[0] - self.positions[name][0]) > t_tol or \
               abs(pos[1] - self.positions[name][1]) > t_tol or \
               abs(pos[2] - self.positions[name][2]) > t_tol or \
               abs(quat[0] - self.positions[name][3]) > r_tol or \
               abs(quat[1] - self.positions[name][4]) > r_tol or \
               abs(quat[2] - self.positions[name][5]) > r_tol or \
               abs(quat[3] - self.positions[name][6]) > r_tol

    def add_to_frame(self, name, pos, quat):
        """Update an objects position by adding its new transform to
        the current frame.

        This function will only have an effect if the given object
        has moved since the last time its transform was updated. Meaning,
        you can safely call this method every frame even if the object
        has not moved.

        pos  : translation
        quat : rotation as quaternion (qx, qy, qz, qw)
        """
        if self.enough_motion(name, pos, quat):
            self.log_data["frames"][-1][name] = {
                "t": pos,
                "r": quat,
            }
            self.positions[name] = list(pos) + list(quat)

    def add_frame(self, name, pos, quat):
        """A method for adding a single object to the frame.

        For most use cases, you will want to manually create a frame,
        and then add indvividual objects to the frame.
        """
        self.new_frame()
        self.add_to_frame(name, pos, quat)

    def to_string(self, compact=False):
        """Convert logged data to a string.

        Set compact=True if you want to minimize the json output.
        """
        if compact:
            return json.dumps(self.log_data, separators=(",", ":"))
        else:
            return json.dumps(self.log_data, sort_keys=True, indent=4)

    def __str__(self):
        """Convert logged data to a string."""
        return self.to_string()
