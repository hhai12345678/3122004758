import sys
import difflib


def compute_similarity(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        text1 = file1.read()
        text2 = file2.read()

    # 使用 difflib 计算相似度
    sequence = difflib.SequenceMatcher(None, text1, text2)
    return sequence.ratio()

if __name__ == '__main__':
    # 接受命令行参数
    if len(sys.argv) != 4:
        print("Usage: python main.py <orig_file> <plagiarized_file> <output_file>")
        sys.exit(1)

    orig_file = sys.argv[1]
    plag_file = sys.argv[2]
    output_file = sys.argv[3]

    # 计算重复率
    similarity = compute_similarity(orig_file, plag_file)

    # 输出结果到答案文件，保留两位小数
    with open(output_file, 'w') as result_file:
        result_file.write(f"{similarity:.2f}")


