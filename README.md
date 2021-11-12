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
This is the Linux branch. For windows support, see the `main` branch.

The Python code can be cloned and installed as follows:

```
git clone https://github.com/wholden/zwo-efw.git
python setup.py install
```

The drivers must be downloaded directly from ZWO. Choose the "Developers" tab and download the SDK for "Linux & Mac" EFW.
https://astronomy-imaging-camera.com/software-drivers

Extract and place the `libEFWFilter.so.1.7`" and `EFW_Filter.h` files in the "zwo_efw/lib" folder. Then follow the instructions in the next section.

## Build Instructions for Linux
1. For Linux to work with CFFI, we need to be able to link to udev. This requires that the udev shared library be installed. 
   * On ubuntu: `sudo apt install libudev-dev`

2. For the linking to work properly, we have to change how we are using CFFI (compared to `main` branch). Instead of dynamically interacting with the library, we have to use CFFI to build a python extension that is linked.
   * This just requires running the command below which will generate `_efw_api.c` and `_efw_api.o` and a file like `_efw_api.cpython-37m-x86_64-linux-gnu.so`
   * The command to run is:
      * `python efw_build.py` 

## Working with raspberry pi (armv8)
While the above tentatively worked for me on an x64 Ubuntu system, additional steps are needed for working with raspberry pi (armv8). 

### Build/Install Package

```bash
python setup.py sdist
pip install ./dist/zwo_efw-1.0.tar.gz
```

### Link Libraries

```bash
sudo vi /etc/ld.so.conf
```

At this configuration file please add the path to the `lib` folder of zwo_efw (e.g. `/PYTHON_VENV_PATH/lib/python3.7/site-packages/zwo_efw/lib`). Then run:


```bash
ldconfig
```

 ---
Refer to [this issue](https://github.com/wholden/zwo-efw/issues/1) for detail on how user @APinto-DTx got it working.
