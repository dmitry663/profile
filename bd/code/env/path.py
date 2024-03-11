# 경로:env/path.py

import os

# 파일 공유앱 이름
app_name = "FileShareApp"
# 사용자의 홈 디렉토리 경로 가져오기
home_directory = os.path.expanduser("~")

# 사용자의 로컬 데이터를 저장하는 디렉토리 경로
local_data_directory = os.path.join(home_directory, "AppData", "Local", "Dmitry663")

# 파일 공유앱 데이터를 저장하는 디렉토리 경로
file_share_app_directory = os.path.join(local_data_directory, "FileShareApp")

# 개발자의 깃허브 아이디
developer = "dmitry663"

# 개발자의 깃허브 주소
developer_github = f"https://github.com/{developer}"

# 깃허브 원시 파일 주소
raw_file = f"https://raw.githubusercontent.com:443/{developer}/{app_name}/main"


f"https://raw.githubusercontent.com/dmitry663/FileShareApp/main"