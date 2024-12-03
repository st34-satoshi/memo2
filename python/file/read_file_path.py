import os
import argparse

def get_all_files(directory):
    """
    指定したディレクトリ内のすべてのファイルを再帰的に取得する
    
    Args:
        directory (str): 検索対象のディレクトリパス
        
    Returns:
        list: ファイルパスのリスト
    """
    files = []
    
    # 除外するファイル名やディレクトリ名のリスト
    excluded_names = ['.git', '__pycache__', '.vscode', '.idea', 'venv']
    
    # ディレクトリ内のすべてのファイルとディレクトリを取得
    for entry in os.listdir(directory):
        # 除外リストに含まれる名前はスキップ
        full_entry_path = os.path.join(directory, entry)
        if any(excluded in full_entry_path for excluded in excluded_names):
            continue
        full_path = os.path.join(directory, entry)
        
        if os.path.isfile(full_path):
            # ファイルの場合はリストに追加
            files.append(full_path)
        elif os.path.isdir(full_path):
            # ディレクトリの場合は再帰的に処理
            files.extend(get_all_files(full_path))
    return files

def read_file_content(file_path):
    """
    ファイルの中身を読み取ってテキストで返す
    
    Args:
        file_path (str): 読み取るファイルのパス
        
    Returns:
        str: ファイルの内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            start = f"----{file_path} START----\n"
            content = f.read()
            end = f"----{file_path} END----\n\n"
            return f"{start}{content}\n{end}"
    
    except Exception as e:
        print(f"\033[31m[エラー: ファイルを読み込めませんでした。file: {file_path}, error: {str(e)}]\033[0m")
        return ""

def write_file_content(file_path, content):
    """
    テキストをファイルに書き込む
    
    Args:
        file_path (str): 書き込み先のファイルパス
        content (str): 書き込むテキスト内容
        
    Returns:
        bool: 書き込みが成功したかどうか
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"\033[31m[エラー: ファイルに書き込めませんでした。file: {file_path}, error: {str(e)}]\033[0m")
        return False


if __name__ == "__main__":
    # 使用例
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_dir', default="./", help="Target directory path")
    parser.add_argument('--ignore-if-includes', nargs='+', default=[], 
                      help="List of strings to exclude files if they contain any of these")
    args = parser.parse_args()
    directory = args.target_dir  # カレントディレクトリ
    print(directory)
    print(args.ignore_if_includes)
    files = get_all_files(directory)
    print(files)
    summary_text = ""
    for f in files:
        summary_text += read_file_content(f)
    # print(summary_text)
    write_file_content("summary.txt", summary_text)
