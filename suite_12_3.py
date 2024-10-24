import unittest
import tests_12_1
import tests_12_2
#import tests_12_3

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)