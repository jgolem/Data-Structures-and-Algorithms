import random
import unittest


def generate_random_number_list(length):
    values = []
    for i in range(length):
        values.append(random.randint(0, 1000000))
    return values

class test_BubbleSort(unittest.TestCase):
    def tests(self):
        values = generate_random_number_list(10)
        print(values)

        self.assertEqual()