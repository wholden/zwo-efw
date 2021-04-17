from ._cffi import efw, ffi
from .error import check_error


def get_number_of_devices():
    return efw.EFWGetNum()


def get_product_ids():
    num = get_number_of_devices()
    ids = ffi.new(f'int [{num}]')
    efw.EFWGetProductIDs(ids)
    return list(ids)


def get_id(index):
    efwid = ffi.new('int*')
    code = efw.EFWGetID(index, efwid)
    check_error(code)
    return efwid[0]


def open(efwid):
    code = efw.EFWOpen(efwid)
    check_error(code)


def get_property(efwid):
    info = ffi.new('EFW_INFO *')
    code = efw.EFWGetProperty(efwid, info)
    check_error(code)
    res = {
        'ID': info.ID,
        'Name': b''.join(info.Name).decode('utf-8').strip('\x00'),
        'slotNum': info.slotNum
    }
    return res


def get_position(efwid):
    pos = ffi.new('int *')
    code = efw.EFWGetPosition(efwid, pos)
    check_error(code)
    return pos[0]


def set_position(efwid, pos):
    code = efw.EFWSetPosition(efwid, pos)
    check_error(code)


def set_direction(efwid, bool_dir):
    code = efw.EFWSetDirection(efwid, bool_dir)
    check_error(code)


def get_direction(efwid):
    bool_dir = ffi.new('bool *')
    code = efw.EFWGetDirection(efwid, bool_dir)
    check_error(code)
    return bool_dir[0]


def calibrate(efwid):
    code = efw.EFWCalibrate(efwid)
    check_error(code)


def close(efwid):
    efw.EFWClose(efwid)


def get_sdk_version():
    raise NotImplementedError
    # return efw.EFWGetSDKVersion()


def get_hw_error_code(efwid):
    hw_err = ffi.new('int *')
    code = efw.EFWGetHWErrorCode(efwid, hw_err)
    check_error(code)
    return hw_err[0]


def get_firmware_version(efwid):
    major = ffi.new('unsigned char *')
    minor = ffi.new('unsigned char *')
    build = ffi.new('unsigned char *')
    code = efw.EFWGetFirmwareVersion(efwid, major, minor, build)
    check_error(code)
    return major[0], minor[0], build[0]


def get_serial_number(efwid):
    serial = ffi.new('EFW_SN *')
    code = efw.EFWGetSerialNumber(efwid, serial)
    check_error(code)
    return serial


def set_id(efwid):
    raise NotImplementedError
#     efw.EFWSetID(efwid, alias)
