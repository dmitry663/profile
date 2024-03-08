from library.development_tools import dev_print

development_mode_enabled = True

if run_executable(executable_path, arguments):
    dev_print("실행 파일이 성공적으로 실행되었습니다.")
else:
    dev_print("실행 파일 실행 중 오류가 발생했습니다.")

