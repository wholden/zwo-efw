import pathlib
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
     int EFWGetNum(void);
""")

ffibuilder.set_source("_efw_api",
"""
     #include <stdbool.h>
     #include "EFW_filter.h"
""",
     libraries=['EFWFilter', 'udev', 'stdc++'],
     library_dirs=[str(pathlib.Path(__file__).parent)],
     )

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)