import unittest
import task_02_tests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(task_02_tests.FigureTests))
calcTestSuite.addTest(unittest.makeSuite(task_02_tests.CircleTests))
calcTestSuite.addTest(unittest.makeSuite(task_02_tests.TriangleTests))
calcTestSuite.addTest(unittest.makeSuite(task_02_tests.SquareTests))
print(f"count of tests: {str(calcTestSuite.countTestCases())}  \n ")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
