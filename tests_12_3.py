import runner
import unittest
from runner_and_tournament import Runner, Tournament

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
        runner1 = runner.Runner("Бегун 1")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @skip_frozen
    def test_run(self):
        runner2 = runner.Runner("Бегун 2")
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


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_frozen
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты тестов:")
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @skip_frozen
    def test_01(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_frozen
    def test_02(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    @skip_frozen
    def test_03(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

if __name__ == "__main__":
    unittest.main()