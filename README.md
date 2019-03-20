# logger-py

[Falling ball example](https://review.github.io/?log=https://raw.githubusercontent.com/review/logger-py/master/examples/falling_sphere.json)

This library needs to be setup to be pip installable, but the functionality works fine. You can copy the file to your directory and import it, or use the kludge shown in the [example file](https://github.com/review/logger-py/blob/master/examples/falling_sphere.py).

# Ideas

1. Create a context manager instead of manually calling `new_frame()`.
2. Have `add_*` automatically create the initial frame?
3. Make all parameters to `add_*` optional.
