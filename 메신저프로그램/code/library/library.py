from library.env import *
# 개발 중에만 출력을 하는 함수
def dev_print(*args, **kwargs):
    # 개발 중에만 출력을 하는 조건을 추가할 수 있습니다.
    if development_mode_enabled:
        print(*args, **kwargs)


import os

def get_messenger_path():
    # 사용자의 홈 디렉토리 가져오기
    home_directory = os.path.expanduser("~")

    # 메신저 경로 생성
    messenger_path = os.path.join(home_directory, "AppData", "Local", "Dmitry663", "Messenger")

    return messenger_path


import os

def ensure_folder_exists(folder_path):
    # 폴더가 존재하는지 확인
    if not os.path.exists(folder_path):
        print(f"{folder_path} 폴더가 존재하지 않습니다. 폴더를 생성합니다.")
        try:
            # 폴더 생성
            os.makedirs(folder_path)
            print(f"{folder_path} 폴더를 생성했습니다.")
        except OSError as e:
            print(f"폴더를 생성하는 도중 에러가 발생했습니다: {e}")
    else:
        print(f"{folder_path} 폴더가 이미 존재합니다.")
