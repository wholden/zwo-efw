For Linux to work with CFFI, we need to be able to link to udev.
This requires that the udev shared library be installed. On ubuntu: `sudo apt install libudev-dev`

For the linking to work properly, we have to change how we are using CFFI. Instead of dynamically interacting with the library, we have to use CFFI to build a python extension that is linked.

It should be as simple as: `python efw_build.py` which will generate `_efw_api.c` and `_efw_api.o` and a file like `_efw_api.cpython-37m-x86_64-linux-gnu.so`

Then access to the library functions will look like:
```python
from _efw_api import ffi, lib

lib.EFWGetNum()
```

Next steps, I will add the extra function headers to the `efw_build.py` and then rewrite the other modules to properly use this new backend.
