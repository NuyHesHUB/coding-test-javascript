import os
import git
from datetime import datetime
import subprocess
import codecs
import urllib.parse

# 리포지토리 경로
repo_path = '.'

README_PATH = os.path.join(repo_path, 'README.md')
REPO_URL = 'https://github.com/NuyHesHUB/coding-test-javascript/tree/main'

def get_latest_pushed_commit_hash():
    try:
        # 최신 푸시된 커밋의 해시를 가져옵니다.
        latest_commit_hash = subprocess.check_output(['git', 'log', 'origin/main', '-1', '--pretty=format:%H'], cwd=repo_path).decode('utf-8').strip()
        print(f"Latest pushed commit hash: {latest_commit_hash}")
        return latest_commit_hash
    except subprocess.CalledProcessError as e:
        print(f"Git Command Error: {e}")
        return None  # 오류가 발생하면 None을 반환합니다.
    
def get_latest_file_path():
    try:
        latest_commit_hash = get_latest_pushed_commit_hash()
        if not latest_commit_hash:
            return None

        # 최신 푸시된 커밋의 변경된 파일 목록을 가져옵니다.
        changed_files = subprocess.check_output(['git', 'show', '--pretty=', '--name-only', latest_commit_hash], cwd=repo_path).decode('utf-8').strip().split('\n')

        # 최근 hash 값으로 git show --pretty="" --name-only {hash} 명령어를 실행하여 변경된 파일 목록을 가져옵니다.

        
        print(f"Changed files: {changed_files}")

        # 변경된 파일 중 JavaScript 파일을 찾습니다.
        for file_path in changed_files:
            print(f"file_path: {file_path}")
            decoded_path = codecs.decode(file_path.strip('"'), 'unicode_escape')  # 파일 경로를 디코딩하고 따옴표를 제거합니다.
            if decoded_path.endswith('.js'):
                print(f"JavaScript file found: {decoded_path}")
                return decoded_path
            
    except subprocess.CalledProcessError as e:
        print(f"Git Command Error: {e}")
        return None  # 오류가 발생하면 None을 반환합니다.
    
    print("No JavaScript file found in the latest commit.")
    return None  # js 파일이 없으면 None을 반환합니다.

def get_new_entry(file_path):
    # 파일 경로에서 디렉토리만 추출
    parts = file_path.split('/')
    date = datetime.now().strftime('%Y-%m-%d')
    platform = urllib.parse.unquote(parts[-4])
    level = urllib.parse.unquote(parts[-3])
    title = urllib.parse.unquote(parts[-2])

    decoded_title = title.encode('latin1').decode('utf-8')
    transform_title = decoded_title.replace(' ', '%20')

    url = f"{REPO_URL}/{platform}/{level}/{transform_title}"

    return f"| {date} | {level} | {decoded_title} | [바로가기]({url}) |"

def update_readme(new_entry):
    with open(README_PATH, 'a', encoding='utf-8') as readme_file:
        readme_file.write(f"{new_entry}\n")

# Run the function and print the result
file_path = get_latest_file_path()
if file_path:
    print(f"Latest JavaScript file path: {file_path}")
    new_entry = get_new_entry(file_path)
    print(f"New entry: {new_entry}")
    update_readme(new_entry)
else:
    print("No JavaScript file found.")