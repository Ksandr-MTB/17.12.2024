import logging
from unittest import TestCase
from rt_with_exceptions import Runner
import unittest


class RunnerTest(TestCase):


    def test_walk(self):
        try:
            object_1 = Runner('12', speed=-10)
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info(f'"test_walk" выполнен успешно Имя={object_1} скорость= {object_1.speed}')




    def test_run(self):
        try:
            object_1 = Runner(45, speed=12)

        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info(f'"test_run" выполнен успешно Имя={object_1} скорость={object_1.speed}')


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format="%(levelname)s | %(message)s | %(asctime)s")


