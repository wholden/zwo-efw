ERROR_CODES = {
    0: "EFW_SUCCESS",# = 0,
    1: "EFW_ERROR_INVALID_INDEX",#,
    3: "EFW_ERROR_INVALID_ID",#,
    4: "EFW_ERROR_INVALID_VALUE",#,
    5: "EFW_ERROR_REMOVED",#, //failed to find the filter wheel, maybe the filter wheel has been removed
    6: "EFW_ERROR_MOVING",#,//filter wheel is moving
    7: "EFW_ERROR_ERROR_STATE",#,//filter wheel is in error state
    8: "EFW_ERROR_GENERAL_ERROR",#,//other error
    9: "EFW_ERROR_NOT_SUPPORTED",#,
    10: "EFW_ERROR_CLOSED",#,
    -1: "EFW_ERROR_END",# = -1
}


class EFWError(IOError):

    def __init__(self, errno):
        self.errno = errno

    def __str__(self):
    #     s = '[EFWError {}] {}'.format(self.errno, self.strerror)

        return f'EFWError {self.errno}: {ERROR_CODES[self.errno]}'

    @classmethod
    def from_errno(cls, errno):
        return cls(errno)


def check_error(errno):
    if errno != 0:
        raise EFWError.from_errno(errno)
