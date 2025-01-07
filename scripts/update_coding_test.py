import os
import git
from datetime import datetime
import subprocess


# 커밋 날짜를 가져오는 함수
def get_commit_date(repo_path):
    repo = git.Repo(repo_path)
    commit = repo.head.commit
    return commit.committed_datetime.strftime('%Y-%m-%d')  # YYYY-MM-DD 형식


# 변경된 파일 목록을 가져오는 함수
def get_changed_files():
    # 최근 커밋과 그 이전 커밋 간의 변경된 파일 목록 가져오기
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 명령어가 성공적으로 실행되었는지 확인
    if result.returncode != 0:
        print(f"Error executing git diff: {result.stderr}")
        return []

    # 변경된 파일들을 줄바꿈으로 나누어 리스트로 반환
    changed_files = result.stdout.splitlines()
    print("Changed files:", changed_files)  # 디버깅용 로그
    return changed_files


# 문제 정보를 추출하는 함수
def extract_problem_info(changed_files):
    problem_list = []
    for file_path in changed_files:
        # 파일 경로에서 문제 정보를 추출
        parts = file_path.split(os.sep)
        print("File path parts:", parts)  # 디버깅용 로그
        if len(parts) >= 3:  # 파일 구조가 최소 Lv.1/문제제목/solution.js이어야 함
            problem_info = {
                "date": get_commit_date(os.getcwd()),  # 커밋 날짜
                "level": parts[-3],                    # 예: Lv.1
                "title": parts[-2],                    # 문제 제목
                "url": f"https://github.com/NuyHesHUB/coding-test-javascript/tree/main/{file_path.replace(os.sep, '/')}"
            }
            problem_list.append(problem_info)
    print("Extracted problem list:", problem_list)  # 디버깅용 로그
    return problem_list


# README.md 파일 업데이트하는 함수
def update_readme(problem_list):
    readme_path = os.path.join(os.getcwd(), 'README.md')

    # README 파일 읽기
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 기존 테이블의 시작 인덱스 확인
    table_start_idx = None
    for i, line in enumerate(content):
        if line.startswith("| 날짜"):
            table_start_idx = i
            break

    # 테이블이 없다면 새로운 테이블 헤더 추가
    if table_start_idx is None:
        content.append("\n### 문제 목록\n\n| 날짜       | 레벨 | 문제 제목                | 바로가기 |\n")
        content.append("|------------|------|--------------------------|----------|\n")
        table_start_idx = len(content) - 1  # 새로운 테이블 헤더 위치 설정

    # 기존 테이블 뒤에 문제 정보 추가
    for problem in problem_list:
        new_row = f"| {problem['date']} | {problem['level']} | {problem['title']} | [바로가기]({problem['url']}) |\n"
        content.insert(table_start_idx + 1, new_row)

    # 수정된 내용을 다시 파일에 저장
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print("README.md updated successfully.")  # 디버깅용 로그


# 메인 실행 부분
changed_files = get_changed_files()  # 변경된 파일들
problem_list = extract_problem_info(changed_files)  # 문제 정보 추출
update_readme(problem_list)  # README.md 업데이트
