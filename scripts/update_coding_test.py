import os
import git
from datetime import datetime
import urllib.parse

# 리포지토리 경로
repo_path = '.'

README_PATH = os.path.join(repo_path, 'README.md')
REPO_URL = 'https://github.com/NuyHesHUB/coding-test-javascript/tree/main'

def get_latest_file_path():
    repo = git.Repo(repo_path)  # 'repo_path' 경로의 Git 리포지토리를 엽니다.
    latest_commit = repo.head.commit  # 현재 브랜치의 최신 커밋을 가져옵니다.

    try:
        # 최신 커밋의 변경된 파일 목록을 가져옵니다.
        for diff in latest_commit.diff('HEAD~1'):
            if diff.a_path.endswith('.js'):  # 변경된 파일이 js 파일인지 확인합니다.
                return diff.a_path  # js 파일의 경로를 반환합니다.
    except git.exc.GitCommandError as e:
        print(f"Git Command Error: {e}")
        return None  # 오류가 발생하면 None을 반환합니다.
    except IndexError:
        print("No previous commit found.")
        return None  # 이전 커밋이 없으면 None을 반환합니다.
    
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
