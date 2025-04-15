import os
import shutil

# 다운로드 폴더 경로
download_dir = r'c:\Users\student\Downloads'

# 이동할 폴더 경로들
dest_dirs = {
    'images': ['.jpg', '.jpeg'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

# 폴더 생성 및 파일 이동
for folder, extensions in dest_dirs.items():
    dest_path = os.path.join(download_dir, folder)
    os.makedirs(dest_path, exist_ok=True)  # 폴더 없으면 생성

    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                try:
                    shutil.move(file_path, os.path.join(dest_path, filename))
                    print(f'Moved: {filename} -> {folder}')
                except Exception as e:
                    print(f'Error moving {filename}: {e}')
