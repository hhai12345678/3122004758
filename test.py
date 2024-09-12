import unittest
from main import compute_similarity


class TestPlagiarismChecker(unittest.TestCase):

    def setUp(self):
        """
        设置测试环境，每次测试之前运行。
        - 定义原文文件和不同版本抄袭文档的路径。
        - 创建一个空文件，用于测试与空文件之间的相似度。
        """
        # 原文文件路径
        self.orig_file = 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig.txt'

        # 抄袭版本文件路径
        self.plag_files = {
            'add': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_add.txt',
            'del': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_del.txt',
            'dis_1': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_1.txt',
            'dis_10': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_10.txt',
            'dis_15': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_15.txt',
        }

        # 空文件路径
        self.empty_file = 'C:/Users/25406/PycharmProjects/pythonProject8/demo/empty.txt'

        # 创建一个空文件供测试
        with open(self.empty_file, 'w', encoding='utf-8') as f:
            f.write("")

    def test_exact_match(self):
        """
        测试原文文件和自身对比，期望相似度为 1.0（完全相同）。
        """
        similarity = compute_similarity(self.orig_file, self.orig_file)
        self.assertAlmostEqual(similarity, 1.0, places=2)  # 相似度应接近1.0

    def test_add_file_similarity(self):
        """
        测试抄袭文件 orig_0.8_add.txt 与原文的相似度。
        该抄袭文件应该与原文有较大相似度，但不会完全相同，期望在 0.7 到 1.0 之间。
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['add'])
        self.assertGreater(similarity, 0.7)  # 相似度大于0.7
        self.assertLess(similarity, 1.0)  # 相似度小于1.0

    def test_del_file_similarity(self):
        """
        测试抄袭文件 orig_0.8_del.txt 与原文的相似度。
        该抄袭文件删除了一些内容，期望相似度在 0.7 到 1.0 之间。
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['del'])
        self.assertGreater(similarity, 0.7)  # 相似度大于0.7
        self.assertLess(similarity, 1.0)  # 相似度小于1.0

    def test_dis_1_file_similarity(self):
        """
        测试抄袭文件 orig_0.8_dis_1.txt 与原文的相似度。
        该文件有一些小的不同，期望相似度在 0.6 到 0.95 之间。
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_1'])
        self.assertGreater(similarity, 0.6)  # 相似度大于0.6
        self.assertLess(similarity, 0.95)  # 相似度小于0.95

    def test_dis_10_file_similarity(self):
        """
        测试抄袭文件 orig_0.8_dis_10.txt 与原文的相似度。
        该文件有更多不同，期望相似度在 0.5 到 0.8 之间。
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_10'])
        self.assertGreater(similarity, 0.5)  # 相似度大于0.5
        self.assertLess(similarity, 0.8)  # 相似度小于0.8

    def test_dis_15_file_similarity(self):
        """
        测试抄袭文件 orig_0.8_dis_15.txt 与原文的相似度。
        该文件有更多修改，期望相似度在 0.5 到 0.8 之间。
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_15'])
        self.assertGreater(similarity, 0.5)  # 相似度大于0.5
        self.assertLess(similarity, 0.8)  # 相似度小于0.8

    def test_empty_file_vs_original(self):
        """
        测试空文件与原文文件的相似度，期望为 0.0。
        """
        similarity = compute_similarity(self.orig_file, self.empty_file)
        self.assertEqual(similarity, 0.0)  # 相似度应为0.0

    def test_empty_file_vs_empty(self):
        """
        测试两个空文件之间的相似度，期望为 1.0。
        """
        similarity = compute_similarity(self.empty_file, self.empty_file)
        self.assertAlmostEqual(similarity, 1.0, places=2)  # 相似度应为1.0


if __name__ == '__main__':
    unittest.main()
