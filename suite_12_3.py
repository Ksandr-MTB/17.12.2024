import unittest
# import module_12_1
# import module_12_2_
import tests_12_3


runnerTS_R = unittest.TestSuite()
runnerTS_T = unittest.TestSuite()
# runnerTS_R.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
# runnerTS_T.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_.TournamentTest))

runnerTS_R.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnerTS_T.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))



runner = unittest.TextTestRunner(verbosity = 2)
runner.run(runnerTS_R)
runner.run(runnerTS_T)