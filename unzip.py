import os
import zipfile

# 압축 파일이 있는 디렉터리 경로 설정
directory = r"C:/Users/aweso/Project/samurai/samurai/data/LaSOT"

# 디렉터리 내 모든 파일 확인
for file in os.listdir(directory):
    # 파일이 .zip 확장자를 가지는 경우
    if file.endswith(".zip"):
        zip_path = os.path.join(directory, file)  # .zip 파일 경로
        extract_path = os.path.join(directory, os.path.splitext(file)[0])  # 압축 해제 경로

        # 압축 해제 디렉터리가 이미 존재하지 않으면 압축 해제
        if not os.path.exists(extract_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                print(f"Extracting {file}...")
                zip_ref.extractall(extract_path)
        else:
            print(f"{extract_path} already exists, skipping...")

print("All zip files have been extracted.")
