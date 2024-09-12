import sys  # 导入 sys 模块，用于读取命令行参数
import difflib  # 导入 difflib 库，用于计算两个文本之间的相似度

def compute_similarity(file1_path, file2_path):
    """
    计算两个文件的相似度
    :param file1_path: 原文文件的路径
    :param file2_path: 抄袭文件的路径
    :return: 两个文件文本内容的相似度，值在 0 到 1 之间
    """
    # 打开文件并读取内容
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        text1 = file1.read()  # 读取第一个文件的全部内容
        text2 = file2.read()  # 读取第二个文件的全部内容

    # 使用 difflib.SequenceMatcher 来比较两个文本的相似度
    # None 表示不使用自定义的相似度比较规则，直接使用默认的字符比较
    sequence = difflib.SequenceMatcher(None, text1, text2)

    # 返回相似度比例，返回值在 0（完全不同）到 1（完全相同）之间
    return sequence.ratio()

if __name__ == '__main__':
    """
    主程序入口，使用命令行参数来指定文件路径，并调用 compute_similarity 计算相似度。
    结果将被写入到指定的输出文件中。
    """
    # 检查命令行参数的数量，确保提供了 3 个参数：原文文件、抄袭版文件和输出文件
    if len(sys.argv) != 4:
        # 如果参数不足或超过，给出正确的使用说明并退出程序
        print("Usage: python main.py <orig_file> <plagiarized_file> <output_file>")
        sys.exit(1)  # 退出程序，返回代码 1 表示有错误

    # 从命令行获取文件路径参数
    orig_file = sys.argv[1]  # 获取第一个参数，原文文件路径
    plag_file = sys.argv[2]  # 获取第二个参数，抄袭版文件路径
    output_file = sys.argv[3]  # 获取第三个参数，输出结果的文件路径

    # 计算两个文件的相似度
    similarity = compute_similarity(orig_file, plag_file)

    # 打开输出文件，将结果写入其中
    # 保留两位小数，表示相似度的结果
    with open(output_file, 'w') as result_file:
        result_file.write(f"{similarity:.2f}")  # 将相似度写入输出文件，保留两位小数
