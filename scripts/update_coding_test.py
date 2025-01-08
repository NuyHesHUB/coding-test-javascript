import os
import git
from datetime import datetime
import urllib.parse
import subprocess

# 리포지토리 경로
repo_path = '.'

README_PATH = os.path.join(repo_path, 'README.md')
REPO_URL = 'https://github.com/NuyHesHUB/coding-test-javascript/tree/main'

def get_latest_file_path():
    try:
        # 최신 커밋의 해시를 가져옵니다.
        latest_commit_hash = subprocess.check_output(['git', 'log', '-1', '--pretty=format:%H'], cwd=repo_path).decode('utf-8').strip()
        print(f"Latest commit hash: {latest_commit_hash}")

        # 최신 커밋의 변경된 파일 목록을 가져옵니다.
        changed_files = subprocess.check_output(['git', 'show', '--pretty=', '--name-only', latest_commit_hash], cwd=repo_path).decode('utf-8').strip().split('\n')
        print(f"Changed files: {changed_files}")

        # 변경된 파일 중 JavaScript 파일을 찾습니다.
        for file_path in changed_files:
            if file_path.endswith('.js'):
                print(f"JavaScript file found: {file_path}")
                return file_path
    except subprocess.CalledProcessError as e:
        print(f"Git Command Error: {e}")
        return None  # 오류가 발생하면 None을 반환합니다.
    
    print("No JavaScript file found in the latest commit.")
    return None  # js 파일이 없으면 None을 반환합니다.
    

def get_new_entry(file_path):
    # 파일 경로에서 디렉토리만 추출
    parts = file_path.split('/')
    date = datetime.now().strftime('%Y-%m-%d')
    platform = parts[-4]
    level = parts[-3]
    title = parts[-2]
    encoded_title = urllib.parse.quote(title)
    link = f'{REPO_URL}/{platform}/{level}/{encoded_title}'

    return {
        'date': date,
        'platform': platform,
        'level': level,
        'title': title,
        'link': link
    }

def update_readme(new_entry):
    # README 파일의 현재 내용을 읽어옵니다.
    with open(README_PATH, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()

    # 새로운 항목을 삽입할 인덱스를 찾습니다.
    for i, line in enumerate(lines):
        if line.startswith('| 날짜'):
            insert_index = i + 2
            break

    # 새로운 항목 라인을 생성합니다.
    new_line = f"| {new_entry['date']} | {new_entry['level']} | {new_entry['title']} | [바로가기]({new_entry['link']}) |\n"

    # 새로운 항목을 라인에 삽입합니다
    lines.insert(insert_index, new_line)

    with open(README_PATH, 'w', encoding = 'utf-8') as file:
        file.writelines(lines)

if __name__ == "__main__":
    file_path = get_latest_file_path() # 최신 커밋에서 변경된 js 파일의 경로를 가져옵니다.

    if file_path:
        new_entry = get_new_entry(file_path) # 리드미에 추가할 객체 data, level, title 등을 가져옵니다.
        update_readme(new_entry)
    else:
        print("No new JavaScript file found.")
