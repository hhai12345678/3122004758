import unittest
from main import compute_similarity
import os

class TestPlagiarismChecker(unittest.TestCase):

    def setUp(self):
        """
        设置测试文件路径，初始化原文和抄袭文件路径
        """
        self.base_path = 'C:/Users/25406/PycharmProjects/pythonProject8/demo/'
        self.orig_file = os.path.join(self.base_path, 'orig.txt')
        self.plag_files = [
            os.path.join(self.base_path, 'orig_0.8_add.txt'),
            os.path.join(self.base_path, 'orig_0.8_del.txt'),
            os.path.join(self.base_path, 'orig_0.8_dis_1.txt'),
            os.path.join(self.base_path, 'orig_0.8_dis_10.txt'),
            os.path.join(self.base_path, 'orig_0.8_dis_15.txt'),
        ]

    def test_exact_match(self):
        """
        测试完全相同的文件
        """
        similarity = compute_similarity(self.orig_file, self.orig_file)
        self.assertAlmostEqual(similarity, 1.0, places=2)

    def test_orig_add_similarity(self):
        """
        测试 orig_0.8_add.txt 与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files[0])
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)

    def test_orig_del_similarity(self):
        """
        测试 orig_0.8_del.txt 与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files[1])
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)

    def test_orig_dis_1_similarity(self):
        """
        测试 orig_0.8_dis_1.txt 与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files[2])
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)

    def test_orig_dis_10_similarity(self):
        """
        测试 orig_0.8_dis_10.txt 与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files[3])
        self.assertGreater(similarity, 0.6)
        self.assertLess(similarity, 0.9)

    def test_orig_dis_15_similarity(self):
        """
        测试 orig_0.8_dis_15.txt 与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files[4])
        self.assertGreater(similarity, 0.5)
        self.assertLess(similarity, 0.8)

if __name__ == '__main__':
    unittest.main()

