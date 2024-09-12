import unittest
from main import compute_similarity

class TestPlagiarismChecker(unittest.TestCase):

    def setUp(self):
        """
        设置测试文件路径
        """
        self.orig_file = 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig.txt'
        self.plag_files = {
            'add': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_add.txt',
            'del': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_del.txt',
            'dis_1': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_1.txt',
            'dis_10': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_10.txt',
            'dis_15': 'C:/Users/25406/PycharmProjects/pythonProject8/demo/orig_0.8_dis_15.txt',
        }
        self.empty_file = 'C:/Users/25406/PycharmProjects/pythonProject8/demo/empty.txt'

        # 创建一个空文件供测试
        with open(self.empty_file, 'w', encoding='utf-8') as f:
            f.write("")

    def test_exact_match(self):
        """
        测试原文和自身对比，期望相似度为 1.0
        """
        similarity = compute_similarity(self.orig_file, self.orig_file)
        self.assertAlmostEqual(similarity, 1.0, places=2)

    def test_add_file_similarity(self):
        """
        测试 orig_0.8_add.txt 文件与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['add'])
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)

    def test_del_file_similarity(self):
        """
        测试 orig_0.8_del.txt 文件与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['del'])
        self.assertGreater(similarity, 0.7)
        self.assertLess(similarity, 1.0)

    def test_dis_1_file_similarity(self):
        """
        测试 orig_0.8_dis_1.txt 文件与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_1'])
        self.assertGreater(similarity, 0.6)
        self.assertLess(similarity, 0.9)

    def test_dis_10_file_similarity(self):
        """
        测试 orig_0.8_dis_10.txt 文件与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_10'])
        self.assertGreater(similarity, 0.5)
        self.assertLess(similarity, 0.8)

    def test_dis_15_file_similarity(self):
        """
        测试 orig_0.8_dis_15.txt 文件与原文的相似度
        """
        similarity = compute_similarity(self.orig_file, self.plag_files['dis_15'])
        self.assertGreater(similarity, 0.5)
        self.assertLess(similarity, 0.8)

    def test_empty_file_vs_original(self):
        """
        测试空文件与原文的相似度，期望为 0.0
        """
        similarity = compute_similarity(self.orig_file, self.empty_file)
        self.assertEqual(similarity, 0.0)

    def test_empty_file_vs_empty(self):
        """
        测试两个空文件之间的相似度，期望为 1.0
        """
        similarity = compute_similarity(self.empty_file, self.empty_file)
        self.assertAlmostEqual(similarity, 1.0, places=2)



    class TestPlagiarismChecker(unittest.TestCase):

        def test_one_word_diff(self):
            """
            测试一个字不同的情况，期望相似度接近 1.0
            """
            text1 = "今天是星期天，天气晴，今天晚上我要去看电影。"
            text2 = "今天是星期天，天气晴，今天晚上我要去看电视。"

            # 创建临时文件用于测试
            with open('temp_text1.txt', 'w', encoding='utf-8') as f:
                f.write(text1)
            with open('temp_text2.txt', 'w', encoding='utf-8') as f:
                f.write(text2)

            similarity = compute_similarity('temp_text1.txt', 'temp_text2.txt')

            # 测试相似度接近 1.0，但不等于 1.0
            self.assertGreater(similarity, 0.9)
            self.assertLess(similarity, 1.0)

        def test_partial_content_match(self):
            """
            测试部分相似的情况，期望相似度为 0.5 到 0.7 之间
            """
            text1 = "今天是星期天，天气晴，今天晚上我要去看电影。"
            text2 = "今天是晴天，我晚上要去看电影。"

            # 创建临时文件用于测试
            with open('temp_text1.txt', 'w', encoding='utf-8') as f:
                f.write(text1)
            with open('partial_match.txt', 'w', encoding='utf-8') as f:
                f.write(text2)

            similarity = compute_similarity('temp_text1.txt', 'partial_match.txt')

            # 测试相似度介于 0.5 到 0.7 之间
            self.assertGreater(similarity, 0.5)
            self.assertLess(similarity, 0.7)

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    unittest.main()
