# 경로:main.py

import os
import sys
import os.path
import requests

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

def isdir(folder):
    return os.path.isdir(folder)

def mkdir(folder):
    print(folder)
    if isdir(folder):
        pass
    elif isdir("\\".join(folder.split('\\')[:-1])):
        os.mkdir(folder)
    else:
        mkdir("\\".join(folder.split('\\')[:-1]))
        os.mkdir(folder)

def main():
    if not os.path.isfile(os.path.join(file_share_app_directory, 'end.config')):
        for file_name in requests.get(f"{raw_file}/config.txt").text.split("\n"):
            response = requests.get(f"{raw_file}/{file_name}")
            mkdir(os.path.dirname(os.path.join(file_share_app_directory, file_name)))
            with open(os.path.join(file_share_app_directory, file_name), 'wb') as file:
                file.write(response.content)

    #if not check_app(file_share_app_directory):
        #download_app(file_share_app_directory, raw_file)
    
    # 다운로드 여부
    # 다운로드

    if len(sys.argv) > 1:
        print([arg for arg in sys.argv])
        #os.system('"C:/Windows/System32/notepad.exe"')
    # 명령 여부
    # 명령

    elif len(sys.argv) == 1:
        print(sys.argv[0])
        #os.system('"C:/Windows/System32/notepad.exe"')

    # 그 외
    # 앱 실행
if __name__ == "__main__":
    main()