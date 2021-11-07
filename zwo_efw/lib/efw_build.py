import pathlib
from cffi import FFI
ffibuilder = FFI()

# Not at all clear why cffi needs this all in cdef instead of pulling it from the header in set_source below...
ffibuilder.cdef("""
     typedef struct _EFW_INFO
     {
          int ID;
          char Name[64];
          int slotNum;
     } EFW_INFO;
     typedef enum _EFW_ERROR_CODE{
          EFW_SUCCESS = 0,
          EFW_ERROR_INVALID_INDEX,
          EFW_ERROR_INVALID_ID,
          EFW_ERROR_INVALID_VALUE,
          EFW_ERROR_REMOVED, //failed to find the filter wheel, maybe the filter wheel has been removed
          EFW_ERROR_MOVING,//filter wheel is moving
          EFW_ERROR_ERROR_STATE,//filter wheel is in error state
          EFW_ERROR_GENERAL_ERROR,//other error
          EFW_ERROR_NOT_SUPPORTED,
          EFW_ERROR_CLOSED,
          EFW_ERROR_END = -1
     }EFW_ERROR_CODE;
     typedef struct _EFW_ID{
          unsigned char id[8];
     }EFW_ID;
     typedef EFW_ID EFW_SN;

     int EFWGetNum(void);
     int EFWGetProductIDs(int* pPIDs);
     EFW_ERROR_CODE EFWGetID(int index, int* ID);
     EFW_ERROR_CODE EFWOpen(int ID);
     EFW_ERROR_CODE EFWGetProperty(int ID, EFW_INFO *pInfo); 
     EFW_ERROR_CODE EFWGetPosition(int ID, int *pPosition);
     EFW_ERROR_CODE EFWSetPosition(int ID, int Position);
     EFW_ERROR_CODE EFWSetDirection(int ID, bool bUnidirectional);
     EFW_ERROR_CODE EFWGetDirection(int ID, bool *bUnidirectional);
     EFW_ERROR_CODE EFWCalibrate(int ID);
     EFW_ERROR_CODE EFWClose(int ID);
     char* EFWGetSDKVersion();
     EFW_ERROR_CODE EFWGetHWErrorCode(int ID, int *pErrCode);
     EFW_ERROR_CODE EFWGetFirmwareVersion(int ID, unsigned char *major, unsigned char *minor, unsigned char *build);
     EFW_ERROR_CODE EFWGetSerialNumber(int ID, EFW_SN* pSN);
     EFW_ERROR_CODE EFWSetID(int ID, EFW_ID alias);
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