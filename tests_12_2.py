import unittest

from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты тестов:")
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_01(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_02(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

    def test_03(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = {place: runner.name for place, runner in result.items()}
        self.assertTrue(result[max(result.keys())].name == "Ник")

if __name__ == "__main__":
    unittest.main()