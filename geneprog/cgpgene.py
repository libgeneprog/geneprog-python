from .api import library
import ctypes

class CGPGene():
	def __init__(self, num_in, num_mid, num_out):
		print("Creating CGPGene")
		self.gene = library.GP_CGP_alloc(num_in, num_mid, num_out).contents
		# Sould also randomize it:
		print("Randomizing CGPGene")
		library.GP_CGP_randomize(self.gene)

	def evaluate(self, inputs):
		print("Evaluating")
		print(self.gene)
		print(self.gene.evaluate)
		outputs = [0,0,0]
		inputs_arr = (ctypes.c_double * len(inputs))(*inputs)
		outputs_arr = (ctypes.c_double * len(outputs))(*outputs)
		data = self.gene.data
		self.gene.evaluate(inputs_arr, outputs_arr, data)
		new_outs = [outputs_arr[i] for i in range(len(outputs))]
		return new_outs