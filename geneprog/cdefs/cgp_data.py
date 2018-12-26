import ctypes

from .gene import GP_Gene

class GP_CGPData(ctypes.Structure):
	_fields_ = [('num_inputs', ctypes.c_uint),
				('num_middle_nodes', ctypes.c_uint),
				('num_outputs', ctypes.c_uint),
				('middle_nodes', ctypes.POINTER(ctypes.c_uint)),
				('output_nodes', ctypes.POINTER(ctypes.c_uint))]

def load(lib):
	#lib.GetImageFromMagickWand.argtypes = [c_void_p]
	#lib.GetImageFromMagickWand.restype = c_void_p
	lib.GP_CGP_alloc.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
	lib.GP_CGP_alloc.restype = ctypes.POINTER(GP_Gene)