import os
from flask import Flask, send_file
from zipfile import ZipFile

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/download">폴더 다운로드</a>'

@app.route('/download')
def download_folder():
    folder_path = 'sample'  # 다운로드할 폴더 경로
    zip_filename = 'downloaded_folder.zip'

    # 폴더를 압축하여 임시로 생성한 압축 파일에 저장
    with ZipFile(zip_filename, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, folder_path)
                zip_file.write(file_path, arcname)

    # 압축 파일을 클라이언트로 전송
    return send_file(zip_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
