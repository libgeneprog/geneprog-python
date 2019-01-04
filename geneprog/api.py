import ctypes
import ctypes.util
from geneprog.cdefs import (cgp_data)


def load_library():
    libgp_path = ctypes.util.find_library('libgeneprog.0.dylib')
    libgp = ctypes.CDLL(str(libgp_path))
    return libgp


library = load_library()
cgp_data.load(library)
