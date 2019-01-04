import ctypes


class GP_Gene(ctypes.Structure):
    _fields_ = [('data', ctypes.c_void_p),
                # void (*evaluate)(double* in, double* out, void* data);
                ('evaluate', ctypes.CFUNCTYPE(None,
                                              ctypes.POINTER(ctypes.c_double),
                                              ctypes.POINTER(ctypes.c_double),
                                              ctypes.c_void_p))]
