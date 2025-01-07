import os
import git
from datetime import datetime
import subprocess

# 커밋 날짜를 가져오는 함수
def get_commit_date(repo_path):
    repo = git.Repo(repo_path)
    commit = repo.head.commit
    return commit.committed_datetime.strftime('%Y-%m-%d')  # YYYY-MM-DD 형식

# 문제 정보를 추출하는 함수
def extract_problem_info(changed_files):
    problem_list = []
    for file_path in changed_files:
        # 파일 경로에서 문제 정보를 추출
        parts = file_path.split(os.sep)
        if len(parts) >= 4:
            problem_info = {
                "date": get_commit_date(os.getcwd()),  # 커밋 날짜
                "level": parts[-3],                    # 예: Lv.1
                "title": parts[-2],                    # 문제 제목
                "url": f"https://github.com/NuyHesHUB/coding-test-javascript/tree/main/{file_path.replace(os.sep, '/')}"
            }
            problem_list.append(problem_info)
    return problem_list

# README.md 파일 업데이트하는 함수
def update_readme(problem_list):
    readme_path = os.path.join(os.getcwd(), 'README.md')

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 기존 내용 찾기
    start_idx = None
    for i, line in enumerate(content):
        if line.startswith("| 날짜"):
            start_idx = i
            break

    # 테이블이 없다면 시작 부분을 찾아서 새로운 테이블을 추가
    if start_idx is None:
        content.append("\n### 문제 목록\n\n| 날짜       | 레벨 | 문제 제목                | 바로가기 |\n|------------|------|--------------------------|----------|\n")

    # 문제 목록을 테이블 형식으로 추가
    for problem in problem_list:
        new_row = f"| {problem['date']} | {problem['level']} | {problem['title']} | [바로가기]({problem['url']}) |\n"
        content.append(new_row)

    # 수정된 내용을 다시 파일에 저장
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(content)

# 커밋된 파일들을 받아오는 함수 (여기서는 간단히 예시로 작성)
def get_changed_files():
   # git diff 명령어를 실행하여 변경된 파일 목록을 얻습니다.
    result = subprocess.run(['git', 'diff', '--name-only'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 명령어가 성공적으로 실행되었는지 확인
    if result.returncode != 0:
        print(f"Error executing git diff: {result.stderr}")
        return []

    # 변경된 파일들을 줄바꿈으로 나누어 리스트로 반환
    changed_files = result.stdout.splitlines()
    return changed_files

# 메인 실행 부분
changed_files = get_changed_files()  # 변경된 파일들
problem_list = extract_problem_info(changed_files)  # 문제 정보 추출
update_readme(problem_list)  # README.md 업데이트
