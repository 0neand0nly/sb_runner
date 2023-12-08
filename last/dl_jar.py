import requests

def download_jar(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

def download_jars_from_file(file_path, output_directory):
    with open(file_path, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                filename = url.split('/')[-1]  # URL의 마지막 부분을 파일 이름으로 사용
                output_path = f"{output_directory}/{filename}"
                download_jar(url, output_path)
                print(f"Downloaded {filename}")

# 사용 예시
input_file_path = 'cln300_url.txt'  # URL이 있는 txt 파일 경로
output_dir = 'vul_jars'  # 다운로드된 파일을 저장할 디렉토리

download_jars_from_file(input_file_path, output_dir)
