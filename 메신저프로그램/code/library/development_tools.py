#현재 개발 중일 경우 True
development_mode_enabled = False

# 개발 중에만 출력을 하는 함수
def dev_print(*args, **kwargs):
    # 개발 중에만 출력을 하는 조건을 추가할 수 있습니다.
    if development_mode_enabled:
        print(*args, **kwargs)
