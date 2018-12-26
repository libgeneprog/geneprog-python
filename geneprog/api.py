import ctypes
import ctypes.util

def load_library():
	libgp_path = ctypes.util.find_library('libgeneprog.0.dylib')
	libgp = ctypes.CDLL(str(libgp_path))
	return libgp

library = load_library()

from geneprog.cdefs import (cgp_data)
cgp_data.load(library)