from unittest import TestCase
from runner import Runner
import runner
import unittest

class RunnerTest(TestCase):

    def test_walk(self):
        test_1 = Runner("Имя")
        for i in range(10):
            test_1.walk()
        self.assertEqual(test_1.distance, 50)


    def test_run(self):
        runner_1 = Runner("Имя")
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)


    def test_challenge(self):
        challenge_walk = Runner('Name1')
        challenge_run = Runner('Name2')
        for i in range(10):
            challenge_walk.walk()
            challenge_run.run()
        self.assertNotEqual(challenge_walk.distance, challenge_run.distance)

