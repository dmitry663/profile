# 경로:main.py
from env.path import file_share_app_directory
import os

def check_app_running():
    # 여기에 해당 앱이 실행 중인지 여부를 체크하는 코드 추가
    # 예를 들어, lock 파일이 존재하는지 여부를 확인할 수 있습니다.
    lock_file_path = os.path.join(file_share_app_directory, "app_lock_file.txt")
    return os.path.exists(lock_file_path)

if __name__ == "__main__":
    # 만약 해당 앱 설정 창이 실행 중이면 앱을 실행하지 않고 종료합니다.
    if check_app_running():
        print("aaaa")
    # 만약 해당 앱 설정 창이 실행 중이 아니면 설정 창을 실행합니다.
    else:
        print("bbbbb")