import os

def count_lines_in_file(file_path):
    """
    计算单个文件的行数。
    :param file_path: 文件路径
    :return: 文件的行数
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except Exception as e:
        print(f"无法读取文件 {file_path}: {e}")
        return 0

def count_lines_in_directory(directory):
    """
    计算目录中所有文件的总行数（包括子目录）。
    :param directory: 目录路径
    :return: 总行数
    """
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_lines += count_lines_in_file(file_path)
    return total_lines

if __name__ == "__main__":
    # 输入目标目录
    target_directory = input("请输入要统计的目录路径: ").strip()
    
    if os.path.isdir(target_directory):
        total_lines = count_lines_in_directory(target_directory)
        print(f"目录 '{target_directory}' 中所有文件的总行数为: {total_lines}")
    else:
        print(f"错误: '{target_directory}' 不是一个有效的目录路径。")
