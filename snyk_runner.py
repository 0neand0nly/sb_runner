import os
import subprocess

# 폴더 경로 설정
folder_path = './vul_train50'

# JAR 파일 경로를 저장할 빈 리스트 생성
jar_file_paths = []

# 폴더 내 모든 파일 및 디렉토리 목록 가져오기
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.jar'):
            jar_file_paths.append(os.path.join(root, file))

# JAR 파일 경로를 기반으로 명령 실행
for jar_file_path in jar_file_paths:
    command = [
        './snyk',
        'test',
        '--scan-unmanaged',
        f'--file={jar_file_path}',
        
    ]
    
    # 명령 실행
    try:
        process = subprocess.Popen(command)
        process.wait()  # 명령이 완료될 때까지 대기
        print(f'Successfully scanned {jar_file_path}')
    except subprocess.CalledProcessError:
        print(f'Failed to scan {jar_file_path}')
