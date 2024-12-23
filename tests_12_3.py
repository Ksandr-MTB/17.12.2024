from unittest import TestCase
from runner import Runner
import unittest


class RunnerTest(TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_1 = Runner("Имя")
        for i in range(10):
            test_1.walk()
        self.assertEqual(test_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = Runner("Имя")
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        challenge_walk = Runner('Name1')
        challenge_run = Runner('Name2')
        for i in range(10):
            challenge_walk.walk()
            challenge_run.run()
        self.assertNotEqual(challenge_walk.distance, challenge_run.distance)


from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrey = Runner("Andrey", speed=9)
        self.nik = Runner("Nik", speed=3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in cls.all_results.items():
            print(f" {place}: {runner} ")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())], self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_nik(self):
        tournament_1 = Tournament(90, self.andrey, self.nik)
        results_1 = tournament_1.start()
        self.all_results.update(results_1)
        self.assertTrue(results_1[max(results_1.keys())], self.nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usain_andrey_nik(self):
        tournament_2 = Tournament(90, self.usain, self.andrey, self.nik)
        results_2 = tournament_2.start()
        self.all_results.update(results_2)
        self.assertTrue(results_2[max(results_2.keys())], self.nik)



if __name__ == '__main__':
    unittest.main()
