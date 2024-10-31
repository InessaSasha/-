import logging
import unittest
import runner
def skip_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return wrapper
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):

        try:
            logging.info(f'"test_walk" выполнен успешно')
            runner1 = runner.Runner("Бегун 1", speed=-10)
        except Exception as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        runner1 = runner.Runner("Бегун 1", speed=10)
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, -50)

    @skip_frozen
    def test_run(self):

        try:
            logging.info(f'"test_run" выполнен успешно')
            runner2 = runner.Runner("Бегун 2", speed='df')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
        runner2 = runner.Runner("Бегун 2", speed='30')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @skip_frozen
    def test_challenge(self):
        runner3 = runner.Runner("Бегун 3")
        runner4 = runner.Runner("Бегун 4")
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                    encoding='UTF-8', format="%(levelname)s| %(message)s")

if __name__ == '__main__':
    unittest.main()
