
import os.path
import requests
import subprocess

def isfile(file):
    return os.path.isfile(file)

def isdir(folder):
    return os.path.isdir(folder)

def isurl(url):
    pass

def isurl(url):
    pass



def check_app(folder):
    if os.path.isfile(os.path.join(folder,'end.config')):
       return True
    return False

def download_app(folder, raw_repository):
    print("file")
    for file in requests.get(f"{raw_repository}/config.txt").text.split("\n"):
        url = f"{raw_repository}/{file}"
        path = f"{folder}\\{file}"
        print(url)
        print(path)
        print(file)
        if not os.path.isdir(os.path.dirname(path)):
            os.mkdir(os.path.dirname(path))
        subprocess.call(['curl', url, '>', path])
