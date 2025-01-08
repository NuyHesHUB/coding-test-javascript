import os
import git
from datetime import datetime
import subprocess
import codecs

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
    platform = parts[-4]
    
    # URL 인코딩 수정
    encoded_parts = [codecs.encode(part, 'unicode_escape').decode('utf-8') for part in parts[:-1]]
    url = f"{REPO_URL}/{'/'.join(encoded_parts)}"
    
    return f"- [{platform}]({url}) - {date}"

# Run the function and print the result
file_path = get_latest_file_path()
if file_path:
    print(f"Latest JavaScript file path: {file_path}")
    new_entry = get_new_entry(file_path)
    print(f"New entry: {new_entry}")
else:
    print("No JavaScript file found.")