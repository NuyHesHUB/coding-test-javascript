import subprocess
import os

def get_latest_commit_hash(repo_path):
    """가장 최근 커밋 해시를 가져옵니다."""
    try:
        latest_commit_hash = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            cwd=repo_path
        ).decode('utf-8').strip()
        return latest_commit_hash
    except subprocess.CalledProcessError as e:
        print(f"Error fetching latest commit hash: {e}")
        return None

def get_changed_files_in_commit(repo_path, commit_hash):
    """특정 커밋에서 변경된 파일 목록을 가져옵니다."""
    try:
        changed_files = subprocess.check_output(
            ['git', 'show', '--pretty=', '--name-only', commit_hash],
            cwd=repo_path
        ).decode('utf-8').strip().split('\n')
        return [file for file in changed_files if file]
    except subprocess.CalledProcessError as e:
        print(f"Error fetching changed files: {e}")
        return []

def extract_programmers_info(file_paths):
    """
    변경된 파일 경로에서 Programmers와 레벨 정보를 추출합니다.
    예: /Programmers/Lv.1/test.js -> 출처: Programmers, 레벨: Lv.1
    """
    extracted_info = []
    for file_path in file_paths:
        parts = file_path.split(os.sep)
        if "Programmers" in parts:
            index = parts.index("Programmers")
            source = parts[index]  # "Programmers"
            level = parts[index + 1] if index + 1 < len(parts) else None  # "Lv.1"
            if level:
                extracted_info.append({"source": source, "level": level})
    return extracted_info

def update_readme_with_programmers_info(repo_path, info):
    """Programmers 정보를 README.md에 업데이트합니다."""
    readme_path = os.path.join(repo_path, 'README.md')
    try:
        # README.md 파일을 열고 업데이트
        with open(readme_path, 'a') as readme_file:
            readme_file.write("\n## Programmers Solutions\n")
            for item in info:
                readme_file.write(f"- {item['source']} - {item['level']}\n")
        print("README.md updated successfully!")
    except Exception as e:
        print(f"Error updating README.md: {e}")

def main(repo_path):
    # Step 1: 최신 커밋 해시 가져오기
    latest_commit_hash = get_latest_commit_hash(repo_path)
    if not latest_commit_hash:
        return

    # Step 2: 변경된 파일 목록 가져오기
    changed_files = get_changed_files_in_commit(repo_path, latest_commit_hash)
    if not changed_files:
        print("No changed files in the latest commit.")
        return

    # Step 3: Programmers와 레벨 정보 추출
    programmers_info = extract_programmers_info(changed_files)
    print(f"Extracted information: {programmers_info}")

    # Step 4: README.md 업데이트
    if programmers_info:
        update_readme_with_programmers_info(repo_path, programmers_info)
    else:
        print("No Programmers-related changes found.")

# 예시 사용
repo_path = "/path/to/your/repo"  # Git 저장소 경로 설정
main(repo_path)