from library.library import *
# 메신저 경로 가져오기
messenger_path = get_messenger_path()
dev_print("메신저 경로:", messenger_path)

ensure_folder_exists(messenger_path)

import json
import os

def read_messenger_info(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                # 파일 내용을 JSON으로 로드
                messenger_info = json.load(file)
                return messenger_info
        except json.JSONDecodeError as e:
            print(f"JSON 디코딩 오류: {e}")
    else:
        print(f"{file_path} 파일이 존재하지 않거나 파일이 아닙니다.")
        return None

# 예제 사용
messenger_info_file = "/path/to/messenger_info.json"
info_data = read_messenger_info(messenger_info_file)

if info_data:
    print("Messenger 정보:")
    print(info_data)