from geneprog.cgpgene import CGPGene

import unittest

class StringUtilTest(unittest.TestCase):
    def test_evaluate(self):
        gene = CGPGene(3,3,3)
        result = gene.evaluate([1,2,3])
        self.assertEqual(result, [0.0, 1.0, 2.0])
