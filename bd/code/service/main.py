import os
import argparse
parser = argparse.ArgumentParser(description="File Share App")

# 서버 포트 지정
parser.add_argument('-p', '--port', type=int, help='서버 포트 번호')

# 공유할 주소 지정
parser.add_argument('-v', '--path', help='공유할 폴더의 주소')

args = parser.parse_args()

data={}
if args.port:
    data['port'] = args.port
else:
    data['port'] = 5000

if args.path:
    data['path'] = args.path
else:
    data['path'] = os.getcwd()



from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from zipfile import ZipFile

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class FileSystemItem:
    def __init__(self, name, is_directory, size=None):
        self.name = name
        self.is_directory = is_directory
        self.size = size

def get_items(path):
    items = os.listdir(path)
    
    # 폴더와 파일을 먼저 정렬하고, 그 후에 글자순으로 정렬
    folders = sorted([item for item in items if os.path.isdir(os.path.join(path, item))])
    files = sorted([item for item in items if not os.path.isdir(os.path.join(path, item))])
    
    items_list = []
    
    # 폴더에 대한 정보를 가져오기
    for folder in folders:
        folder_path = os.path.join(path, folder)
        folder_size = sum(os.path.getsize(os.path.join(folder_path, file)) for file in os.listdir(folder_path))
        items_list.append(FileSystemItem(name=folder, is_directory=True, size=folder_size))
    
    # 파일에 대한 정보를 가져오기
    for file in files:
        file_path = os.path.join(path, file)
        file_size = os.path.getsize(file_path)
        items_list.append(FileSystemItem(name=file, is_directory=False, size=file_size))

    return items_list

def zip_folder(folder_path, zip_path):
    try:
        # 폴더 경로와 압축 파일 경로를 절대 경로로 정규화
        folder_path = os.path.abspath(folder_path)
        zip_path = os.path.abspath(zip_path)

        # 폴더 경로가 존재하는지 확인
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        # 폴더 내용을 압축 파일로 생성
        with ZipFile(zip_path, 'w') as zip_file:
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, folder_path)
                    zip_file.write(file_path, arcname)

    except Exception as e:
        # 오류가 발생하면 예외를 캐치하고 출력
        print(f"An error occurred: {e}")


def clean_up_path(path):
    while '//' in path:
        path = path.replace('//', '/')
    if path.endswith('/') and len(request.path) > 1:
        path = path[:-1]
    return path

app.jinja_env.globals.update(clean_up_path=clean_up_path)

@app.before_request
def add_trailing_slash():
    if '//' in request.path:
        return redirect(request.path.replace('//', '/'))
    if request.path.endswith('/') and len(request.path) > 1:
        return redirect(request.path[:-1])    
    
@app.route('/')
def home():
    return '<a href="/directory">디렉토리로 이동</a>'

@app.route('/directory', strict_slashes=False)
def show_folders_root():
    items = get_items(data['path'])
    return render_template('show_folders.html', path='/', items=items)

@app.route('/directory/<path:folders>', strict_slashes=False)
def show_folders(folders):
    full_path = os.path.join(data['path'], folders)
    items = get_items(full_path)
    return render_template('show_folders.html', path=folders, items=items)

@app.route('/directory/<path:folders>/download', strict_slashes=False)
def download_folders(folders):
    full_path = os.path.join(data['path'], folders)
    # 폴더를 압축하여 임시 파일로 생성
    temp_zip_path = 'temp.zip'
    zip_folder(full_path, temp_zip_path)
    # 압축 파일을 클라이언트에게 전송
    return send_file(os.path.join(data['path'], temp_zip_path), as_attachment=True, download_name=folders+'.zip')


@app.route('/directory/download/<filename>', strict_slashes=False)
def download_file_root(filename):
    return send_from_directory(data['path'], filename, as_attachment=True)

@app.route('/directory/<path:folders>/download/<filename>', strict_slashes=False)
def download_file(folders, filename):
    full_path = os.path.join(data['path'], folders)
    return send_from_directory(full_path, filename, as_attachment=True)

@app.route('/directory/<path:folders>/upload/file', methods=['POST'], strict_slashes=False)
def upload_file(folders):
    print(request.files)
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)
    
    # 파일을 업로드 폴더에 저장
    file.save(os.path.join(os.path.join(data['path'], folders), file.filename))
    
    return "upload_file"

@app.route('/directory/<path:folders>/upload/folder', methods=['POST'], strict_slashes=False)
def upload_folder(folders):
    return "upload_folder"


"""


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    items = get_items(os.getcwd())
    return render_template('show_folders.html', path='/', items=items)

@app.route('/<path:folders>')
def show_folders(folders):
    full_path = os.path.join(os.getcwd(), folders)
    items = get_items(full_path)
    
    return render_template('show_folders.html', path=folders, items=items)

@app.route('/<path:folders>/download/<filename>')
def download_file(folders, filename):
    full_path = os.path.join(os.getcwd(), folders)
    return send_from_directory(full_path, filename, as_attachment=True)

@app.route('/<path:folders>/upload', methods=['POST'])
def upload_file(folders):
    full_path = os.path.join(os.getcwd(), folders)
    
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        file.save(os.path.join(full_path, file.filename))
    
    return redirect(url_for('show_folders', folders=folders))

"""



if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=data['port'], debug=True)