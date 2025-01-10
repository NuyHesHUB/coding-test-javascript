import os
import codecs
import unittest

from unittest.mock import patch, mock_open
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

def get_changed_files_in_commit(repo_path, commit_hash, file_extension='.js'):
    try:
        changed_files = subprocess.check_output(
            ['git', 'show', '--pretty=', '--name-only', commit_hash],
            cwd=repo_path
        ).decode('utf-8').strip().split('\n')
        filtered_files = [file for file in changed_files if file.endswith(file_extension)]

        return filtered_files
    
    except subprocess.CalledProcessError as e:
        print(f"Error fetching changed files: {e}")
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

            class TestUpdateReadme(unittest.TestCase):

                @patch("builtins.open", new_callable=mock_open)
                def test_update_readme_success(self, mock_file):
                    repo_path = '.'
                    info = [
                        {"source": "Programmers", "level": "Lv.1", "title": "문자열 내 p와 y의 개수", "url": "https://github.com/NuyHesHUB/coding-test-javascript/tree/main/Programmers/Lv.1/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98"}
                    ]
                    update_readme(repo_path, info)
                    mock_file.assert_called_once_with(os.path.join(repo_path, 'README.md'), 'a', encoding='utf-8')
                    mock_file().write.assert_called_once_with("| 2025-01-10 | Lv.1 | 문자열 내 p와 y의 개수 | [바로가기](https://github.com/NuyHesHUB/coding-test-javascript/tree/main/Programmers/Lv.1/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98)\n")

                @patch("builtins.open", new_callable=mock_open)
                def test_update_readme_multiple_entries(self, mock_file):
                    repo_path = '.'
                    info = [
                        {"source": "Programmers", "level": "Lv.1", "title": "문자열 내 p와 y의 개수", "url": "https://github.com/NuyHesHUB/coding-test-javascript/tree/main/Programmers/Lv.1/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98"},
                        {"source": "Programmers", "level": "Lv.1", "title": "문자열을 정수로 바꾸기", "url": "https://github.com/NuyHesHUB/coding-test-javascript/tree/main/Programmers/Lv.1/%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%84%20%EC%A0%95%EC%88%98%EB%A1%9C%20%EB%B0%94%EA%BE%B8%EA%B8%B0"}
                    ]
                    update_readme(repo_path, info)
                    mock_file.assert_called_once_with(os.path.join(repo_path, 'README.md'), 'a', encoding='utf-8')
                    self.assertEqual(mock_file().write.call_count, 2)

                @patch("builtins.open", new_callable=mock_open)
                def test_update_readme_fail(self, mock_file):
                    mock_file.side_effect = Exception("File not found")
                    repo_path = '.'
                    info = [
                        {"source": "Programmers", "level": "Lv.1", "title": "문자열 내 p와 y의 개수", "url": "https://github.com/NuyHesHUB/coding-test-javascript/tree/main/Programmers/Lv.1/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%82%B4%20p%EC%99%80%20y%EC%9D%98%20%EA%B0%9C%EC%88%98"}
                    ]
                    with self.assertLogs(level='INFO') as log:
                        update_readme(repo_path, info)
                        self.assertIn("README.md updated fail: File not found", log.output[0])

            if __name__ == '__main__':
                unittest.main()
    changed_files = get_changed_files_in_commit(repo_path, latest_commit_hash, file_extension='.js')