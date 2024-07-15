# reviewlogger

- [Falling ball example](https://review.github.io/?log=https://raw.githubusercontent.com/review/logger-py/master/examples/falling_sphere.json)
- [Morphing box example](https://review.github.io/?log=https://raw.githubusercontent.com/review/logger-py/master/examples/morphing_box.json)

```bash
git clone https://github.com/review/logger-py.git
cd logger-py
python -m pip install .
```

## Ideas

1. Create a context manager instead of manually calling `new_frame()`.
2. Have `add_*` automatically create the initial frame?
3. Make all parameters to `add_*` optional.
4. Automatically update first frame if subsequent frame changes position, rotation, scale, etc.
