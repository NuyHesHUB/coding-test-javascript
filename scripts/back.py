import os
import subprocess

# 문제 리스트를 최상위 README.md에 추가하는 함수
def update_readme(problem_list, readme_path):
    with open(readme_path, 'r+', encoding='utf-8') as file:
        content = file.readlines()
        
        # 마지막에 문제 리스트를 추가
        content.append("\n## 최근 풀었던 문제들\n")
        for problem in problem_list:
            content.append(f"- **{problem['title']}** (Level {problem['level']}): {problem['url']} - {problem['platform_type']} (풀었던 날짜: {problem['date']})\n")
        
        # 파일의 끝에 추가 후 저장
        file.seek(0)
        file.writelines(content)

# 커밋된 파일의 날짜를 가져오는 함수 (YYYY-MM-DD 형식)
def get_commit_date(file_path):
    try:
        result = subprocess.run(
            ['git', 'log', '--date=short', '--format=%cd', file_path],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True,
            check = True
        )
        commit_date = result.stdout.splitlines()[0]
        return commit_date
    
    except subprocess.CalledProcessError as e:
        print(f"Error while getting commit date for {file_path}: {e}")
        return "Unknown"
    
# 변경된 파일에서 문제의 폴더명을 추출하여 문제 리스트를 생성하는 함수
def extract_folder_name(file_paths):
    test_list = []
    for file_path in file_paths:
        # 파일 경로에서 디렉토리만 추출
        dir_path = os.path.dirname(file_path)
        # 디렉토리를 계층적으로 나누기
        parts = dir_path.split(os.sep)
        domain = 'https://github.com/NuyHesHUB/coding-test-javascript/tree/main'
        if len(parts) >= 3:
            platform_type = parts[-3]
            level = parts[-2]
            title = parts[-1]
            date = get_commit_date(file_path)
            url = f'{domain}/{platform_type}/{level}/{title.replace(" ", "%20")}'

            test_list.append({
                'platform_type': platform_type,
                'level': level,
                'title': title,
                'url': url,
                'date': date
            })
    return test_list
