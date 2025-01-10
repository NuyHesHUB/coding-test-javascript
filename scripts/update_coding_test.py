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
            # ['git', 'log', 'origin/main', '-1', '--pretty=format:%H'], 
            ['git', 'rev-parse', 'HEAD'], 
            cwd=repo_path
        ).decode('utf-8').strip()
        print(f"Latest pushed commit hash: {latest_commit_hash}")

        return latest_commit_hash
    
    except subprocess.CalledProcessError as e:
        print(f"Git Command Error: {e}")
        return None

""" def get_changed_files_in_commit(repo_path, commit_hash, file_extension='.js'):
    try:
        print(f"Checking commit: {commit_hash}")

        changed_files = subprocess.check_output(
            ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit_hash],
            cwd=repo_path
        ).decode('utf-8').strip().split('\n')
        
        print(f"Changed files: {changed_files}")

        filtered_files = [file for file in changed_files if file.endswith(file_extension)]
        print(f"Filtered files: {filtered_files}")

        return filtered_files
    
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        return [] """

def get_changed_files_in_commit(repo_path, commit_hash, file_extension='.js'):
    try:
        print(f"Checking commit: {commit_hash}")
        
        # 바이너리 모드로 출력 받기
        process = subprocess.Popen(
            ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit_hash],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, error = process.communicate()
        
        # 디코딩 및 경로 처리
        changed_files = output.decode('utf-8', errors='ignore').strip().split('\n')
        print(f"Raw changed files: {changed_files}")
        
        # 따옴표 제거 및 .js 파일 필터링
        filtered_files = []
        for file in changed_files:
            file = file.strip('"').strip("'")  # 따옴표 제거
            if file and file.endswith(file_extension):
                filtered_files.append(file)
        
        print(f"Filtered files: {filtered_files}")
        return filtered_files
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return []
    
def get_latest_file_path(file_paths):
    extracted_info = []
    for file_path in file_paths:
        parts = file_path.split(os.sep)
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
    
    changed_files = get_changed_files_in_commit(repo_path, latest_commit_hash, file_extension='.js')
    if not changed_files:
        print("No changed files in the latest commit.")
        return
    readme_info = get_latest_file_path(changed_files)
    print(f"Extracted information: {readme_info}")

    if readme_info:
        update_readme(repo_path, readme_info)
    else:
        print("main : not update readme")

main(repo_path)

# 중복된 커밋 방지
# 날짜 커밋기준 날짜