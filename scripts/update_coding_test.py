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

def get_latest_pushed_commit_hash(repo_path):
    try:
        latest_commit_hash = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], 
            cwd=repo_path
        ).decode('utf-8').strip()
        print(f"Latest pushed commit hash: {latest_commit_hash}")

        return latest_commit_hash
    
    except subprocess.CalledProcessError as e:
        print(f"Git Command Error: {e}")
        return None


""" 
$ git diff-tree --no-commit-id --name-only -r da0e76f0ee3a746256aec53e2327f5baa4175d22
Programmers/Lv.1/20 test/20test.js
"""
def get_changed_files_in_commit(repo_path, commit_hash):
    try:
        print(f"Checking commit: {commit_hash}")

        changed_files = subprocess.check_output(
            ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit_hash],
            cwd=repo_path,
        ).decode('utf-8', errors='ignore').strip()

        # 경로에서 큰따옴표 제거
        changed_files = changed_files.replace('"', '')
        # Programmers/Lv.1/\352\260\200\354\232\264\353\215\260 \352\270\200\354\236\220 \352\260\200\354\240\270\354\230\244\352\270\260/test.js
        # txt = '\352\260\200\354\232\264\353\215\260 \352\270\200\354\236\220 \352\260\200\354\240\270\354\230\244\352\270\260'
        txt = '\352\260\200\354\232\264\353\215\260 \352\270\200\354\236\220 \352\260\200\354\240\270\354\230\244\352\270\260'
        test_files = urllib.parse.unquote(txt).encode('latin1').decode('utf-8')
        # changed_files = changed_files.encode('latin1').decode('utf-8')
        # changed_files = changed_files
        # 파일 경로가 여러 줄로 나뉘어 있으므로 split 처리
        changed_files = changed_files.split('\n')

        # print(f"get_changed_files_in_commit : Changed files: {changed_files[0].encode('latin1').decode('utf-8')}")
        print(f"1111111111111get_changed_files_in_commit : Changed files: {test_files}")

        filtered_files = [file for file in changed_files if file.endswith('.js')]
        print(f"get_changed_files_in_commit : Filtered files: {filtered_files}")

        return filtered_files
    
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        return []

def get_latest_file_path(file_paths):
    print(f"file_paths: {file_paths}")

    extracted_info = []

    for file_path in file_paths:
        parts = file_path.split(os.sep)
        print(f"parts: {parts}")

        if len(parts) >= 4:
            """ source = parts[-4]
            level = parts[-3]
            title = parts[-2] """
            source = urllib.parse.unquote(parts[-4])
            level = urllib.parse.unquote(parts[-3])
            # title = urllib.parse.unquote(parts[-2])
            title = parts[-2]

            # decoded_title = title.encode('latin1').decode('utf-8')
            decoded_title = urllib.parse.unquote(title)

            try:
                decoded_title = decoded_title.encode('latin1').decode('utf-8')
            except UnicodeDecodeError:
                pass  # 디코딩 오류가 나면 그냥 건너뜁니다

            transform_title = decoded_title.replace(' ', '%20')
            url = f"{REPO_URL}/{source}/{level}/{transform_title}"

            extracted_info.append({"source": source, "level": level, "title": decoded_title, "url": url})
            print(f"get_latest_file_path file found: {extracted_info}")

    return extracted_info

def update_readme(repo_path, info):
    readme_path = os.path.join(repo_path, 'README.md')

    try:
        # 1. 파일 전체 내용 읽기
        with open(readme_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(readme_path, 'w', encoding='utf-8') as readme_file:

            readme_file.writelines(lines)

            for item in info:
                readme_file.write(f"| 2025-01-10 | {item['level']} | {item['title']} | [바로가기]({item['url']})\n")
                print(f"README.md updated successfully!{readme_file}")
    except Exception as e:
        print(f"README.md updated fail: {e}")

def main(repo_path):
    latest_commit_hash = get_latest_pushed_commit_hash(repo_path)
    if not latest_commit_hash:
        return
    
    # 여기까지 잘나옴

    changed_files = get_changed_files_in_commit(repo_path, latest_commit_hash)

    # print(f"repo_path:{repo_path}, latest_commit_hash:{latest_commit_hash}")
    print(f"changed_files:{changed_files}")

    if not changed_files:
        print("main: not changed_files.")
        return
    
    readme_info = get_latest_file_path(changed_files)
    # 여기서 부터 값이 없음

    print(f"Extracted information: {readme_info}")

    if readme_info:
        update_readme(repo_path, readme_info)
    else:
        print("main : not update readme")

main(repo_path)

# 중복된 커밋 방지
# 날짜 커밋기준 날짜

