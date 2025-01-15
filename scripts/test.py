""" import codecs

# 주어진 경로 문자열
encoded_path = (
    "Programmers/Lv.1/\\352\\260\\200\\354\\232\\264\\353\\215\\260 "
    "\\352\\270\\200\\354\\236\\220 \\352\\260\\200\\354\\240\\270"
    "\\354\\230\\244\\352\\270\\260/test.js"
)

# 유효한 EUC-KR 범위 확인 함수
def is_valid_euc_kr_byte(byte_value):
    return (0xA1 <= byte_value <= 0xFE) or (0x20 <= byte_value <= 0x7E)

# 이스케이프된 8진수 분리 및 변환
def decode_escaped_path(path):
    parts = path.split("\\")  # '\'로 분리
    result = []
    for part in parts:
        if part.isdigit() and len(part) == 3:  # 3자리 숫자일 때만 처리 (8진수)
            try:
                byte_value = int(part, 8)  # 8진수 -> 정수
                if is_valid_euc_kr_byte(byte_value):  # 유효한 바이트인지 확인
                    result.append(bytes([byte_value]))
                else:
                    print(f"유효하지 않은 바이트: {byte_value} (8진수: {part})")
            except ValueError:
                print(f"잘못된 8진수 값: {part}")
        else:
            result.append(part.encode('latin1'))  # 일반 텍스트는 바이트로 변환
    return b"".join(result)  # 바이트 조합

try:
    # 바이트 문자열 생성
    byte_sequence = decode_escaped_path(encoded_path)
    print(f"바이트 데이터: {byte_sequence}")

    # EUC-KR로 디코딩
    decoded_path = codecs.decode(byte_sequence, "euc-kr", errors="replace")
    print(f"디코딩된 문자열: {decoded_path}")

except UnicodeDecodeError as e:
    print(f"디코딩 실패: {e}")
except Exception as e:
    print(f"예상치 못한 오류: {e}") """

import urllib.parse

# https://oliviakim.tistory.com/34

def get_decoded_path(encoded_path):
    parts = encoded_path.split("\\")  # '\'로 분리
    result = []
    for part in parts:
        if part.isdigit() and len(part) == 3:
            try:
                byte_value = int(part, 8)
                result.append(bytes(byte_value))
            except ValueError:
                print(f"Invalid 8-octet value: {part}")
    byte_sequence = bytes(result)
    return byte_sequence

if __name__ == "__main__":
    encoded_path = r'\\352\\260\\200\\354\\232\\264\\353\\215\\260 \\352\\270\\200\\354\\236\\220    \\352\\260\\200\\354\\240\\270\\354\\230\\244\\352\\270\\260'
    # encoded_path = '\\352'
    # encoded_path = '\352\260\200\354\232\264\353\215\260 \352\270\200\354\236\220 \352\260\200\354\240\270\354\230\244\352\270\260'
    result = get_decoded_path(encoded_path)
    
    # Correct decoding chain for Korean text
    try:
        # euc-kr 디코딩을 시도
        decoded_text = result.decode('euc-kr')
        print(f"Decoded Text: {decoded_text}")
        print(f"Length: {len(decoded_text)}")
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")

""" def get_decoded_path(encoded_path):
    # test_files = urllib.parse.unquote(encoded_path).encode('latin1').decode('utf-8')
    test_files = encoded_path.encode('latin1').decode('utf-8')
    
    return test_files

if __name__ == "__main__":
    # encoded_path = '\\352\\260\\200\\354\\232\\264\\353\\215\\260 \\352\\270\\200\\354\\236\\220    \\352\\260\\200\\354\\240\\270\\354\\230\\244\\352\\270\\260'
    # encoded_path = '\\352'
    encoded_path = '\352\260\200\354\232\264\353\215\260 \352\270\200\354\236\220 \352\260\200\354\240\270\354\230\244\352\270\260'
    result = get_decoded_path(encoded_path)
    print(f"Result: {result}")
    print(f"length: {len(result)}") """

    
    
    
""" print(len('\\352'))  # 4를 출력
print(len('\352'))   # 2를 출력 """