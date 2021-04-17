# zwo-efw

Python bindings to control the ZWO electronic filter wheel (EFW) (https://astronomy-imaging-camera.com/product-category/filterfilter-wheel). This library uses cffi to wrap the C headers of the ZWO api. 

## Usage

```python
import zwo_efw

efw = zwo_efw.EFW(efwid=0)
efw.initialize()
efw.get_position() # return current position
efw.set_position(3) # move to position 3 of the filter wheel
```

## Installation
The Python code can be cloned and installed as follows:

```
git clone https://github.com/wholden/zwo-efw.git
python setup.py install
```

The drivers must be downloaded directly from ZWO. Choose the "Developers" tab and download the SDK. Currently only the Windows DLL is supported, but if someone creates a github issue it wouldn't be too hard for me to add linux/mac support.
https://astronomy-imaging-camera.com/software-drivers

The downloaded "EFW_filter.dll" file should be placed in the "zwo_efw/lib" folder.

