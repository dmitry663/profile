import os
import sys

gui_app_name = r'"D:\한창수\dmitry\profile\bd\dist\test.exe"'
service_app_name = r'"D:\한창수\dmitry\profile\bd\dist\test.exe"'

def main():
    if len(sys.argv) > 1:
        os.system(" ".join([service_app_name] + sys.argv[1:]))
    else:
        os.system(gui_app_name)

if __name__=="__main__":
    main()
