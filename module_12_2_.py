import unittest
from unittest import TestCase
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(TestCase):

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

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(results[max(results.keys())], self.nik)

    def test_race_andrey_nik(self):
        tournament_1 = Tournament(90, self.andrey, self.nik)
        results_1 = tournament_1.start()
        self.all_results.update(results_1)
        self.assertTrue(results_1[max(results_1.keys())], self.nik)
    #
    def test_race_usain_andrey_nik(self):
        tournament_2 = Tournament(90, self.usain, self.andrey, self.nik)
        results_2 = tournament_2.start()
        self.all_results.update(results_2)
        self.assertTrue(results_2[max(results_2.keys())], self.nik)



if __name__ == '__main__':
    unittest.main()
