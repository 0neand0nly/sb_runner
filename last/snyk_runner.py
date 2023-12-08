import os
import subprocess

# 폴더 경로 설정
folder_path = './vul_jars'

# JAR 파일 경로를 저장할 빈 리스트 생성
jar_file_paths = []

# 폴더 내 모든 파일 및 디렉토리 목록 가져오기
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.jar'):
            jar_file_paths.append(os.path.join(root, file))

# 결과를 저장할 폴더 생성 (없는 경우)
output_folder = './snyk_results'
os.makedirs(output_folder, exist_ok=True)

# JAR 파일 경로를 기반으로 명령 실행 및 결과 저장
for jar_file_path in jar_file_paths:
    output_file = os.path.join(output_folder, os.path.basename(jar_file_path) + '_snyk_report.txt')
    command = [
        './snyk',
        'test',
        '--scan-unmanaged',
        f'--file={jar_file_path}',
    ]
    
    # 명령 실행 및 결과를 파일에 저장
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
            stdout, _ = process.communicate()
            file.write(stdout)
            print(f'Successfully scanned {jar_file_path} and saved results to {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to scan {jar_file_path}: {e}')
