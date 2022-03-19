# logger-py

- [Falling ball example](https://review.github.io/?log=https://raw.githubusercontent.com/review/logger-py/master/examples/falling_sphere.json)
- [Morphing box example](https://review.github.io/?log=https://raw.githubusercontent.com/review/logger-py/master/examples/morphing_box.json)

This library needs to be setup to be pip installable, but the functionality works fine. You can copy the file to your directory and import it, or use the kludge shown in the [example file](https://github.com/review/logger-py/blob/958bf2271ea48375c33046ee0cf0e104248e83eb/examples/falling_sphere.py#L25).

# Ideas

1. Create a context manager instead of manually calling `new_frame()`.
2. Have `add_*` automatically create the initial frame?
3. Make all parameters to `add_*` optional.
4. Automatically update first frame if subsequent frame changes position, rotation, scale, etc.
