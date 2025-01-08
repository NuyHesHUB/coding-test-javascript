import os
import git
from datetime import datetime
import urllib.parse

# 리포지토리 경로
repo_path = '.'

README_PATH = os.path.join(repo_path, 'README.md')
REPO_URL = 'https://github.com/NuyHesHUB/coding-test-javascript/tree/main'

def get_latest_file_path():
    try:
        repo = git.Repo(repo_path)  # 'repo_path' 경로의 Git 리포지토리를 엽니다.
        commits = list(repo.iter_commits('HEAD'))  # 현재 브랜치의 모든 커밋을 가져옵니다.

        if len(commits) == 0:
            print("No commits in the repository.")
            return None  # 커밋이 없으면 None 반환

        latest_commit = commits[0]  # 최신 커밋

        # 커밋이 하나만 있을 경우, 파일 목록을 직접 반환
        if len(commits) == 1:
            for file in latest_commit.stats.files.keys():
                if file.endswith('.js'):
                    return file
            return None

        # 최신 커밋과 이전 커밋 간의 차이를 확인
        for diff in latest_commit.diff('HEAD~1'):
            if diff.a_path.endswith('.js'):
                return diff.a_path  # js 파일의 경로를 반환
    except git.exc.GitCommandError as e:
        print(f"Git Command Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

    return None  # 변경된 js 파일이 없으면 None 반환
    

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
