if is_folder_exist():
    pass
if is_internet_available():
    pass
if is_folder_hash_matching():
    pass


run_executable()

import subprocess

def run_executable(executable_path, arguments=None):
    """
    주어진 실행 파일을 실행시키는 함수.

    :param executable_path: 실행할 실행 파일 경로
    :param arguments: 실행에 필요한 인자들 (리스트 형태로 전달)
    :return: 실행이 성공하면 True, 그렇지 않으면 False
    """
    try:
        subprocess.run([executable_path] + arguments, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"실행 파일 실행 중 오류가 발생했습니다.")
        return False

# 사용 예제
executable_path = "/path/to/your/executable.exe"
arguments = ["arg1", "arg2"]  # 실행에 필요한 인자들 (필요 없으면 None 또는 빈 리스트로 전달)

if run_executable(executable_path, arguments):
    print("실행 파일이 성공적으로 실행되었습니다.")
else:
    print("실행 파일 실행 중 오류가 발생했습니다.")