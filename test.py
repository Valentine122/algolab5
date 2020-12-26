import unittest

from find_by_boyera_mure import FindByBoyeraMure


class Test(unittest.TestCase):

    def test(self):
        input_string = FindByBoyeraMure("Coronavirus and Virus what is the difference in 2020 ?!")
        self.assertEqual(input_string.search("Virus"), [16])
        self.assertEqual(input_string.search("2020"), [48])

        input_string = FindByBoyeraMure("It's time for adventure !")
        self.assertEqual(input_string.search("time"), [5])
        self.assertEqual(input_string.search("adventure"), [14])


if __name__ == '__main__':
    unittest.main()
