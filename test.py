import unittest

from add import add

class test(unittest.TestCase):
	def testcase1(self):
		self.assertEqual(add(1,2),3)
	def testcase2(self):
		self.assertEqual(add(10,2),12)
	def testcase3(self):
		self.assertEqual(add(5,5),10)
	def testcase4(self):
		self.assertEqual(add(-1,10),9)
		
if __name__ == "__main__":
	unittest.main()
