import unittest
from main import compute_similarity


class TestPlagiarismChecker(unittest.TestCase):
    def test_exact_match(self):
        self.assertAlmostEqual(compute_similarity("C:\Users\25406\PycharmProjects\pythonProject8\demo\orig.txt", 'C:\Users\25406\PycharmProjects\pythonProject8\demo\orig_0.8_add.txt'), 1.0,
                               places=2)

    def test_partial_match(self):
        self.assertAlmostEqual(compute_similarity('test_files/original.txt', 'test_files/partial_copy.txt'), 0.5,
                               places=2)


if __name__ == '__main__':
    unittest.main()
