import unittest
import task_01_tests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(task_01_tests.MyTimeTests))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
