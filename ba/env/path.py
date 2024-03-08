# 경로:env/path.py

import os

# 사용자의 홈 디렉토리 경로 가져오기
home_directory = os.path.expanduser("~")

# 사용자의 로컬 데이터를 저장하는 디렉토리 경로
local_data_directory = os.path.join(home_directory, "AppData", "Local", "Dmitry663")

# 파일 공유앱 데이터를 저장하는 디렉토리 경로
file_share_app_directory = os.path.join(local_data_directory, "FileShareApp")