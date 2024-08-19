from datetime import datetime

readme_file_path = "./study/README.md"

# 현재 날짜 정보 및 위키 링크 생성
today_date_str = datetime.today().strftime('%Y년 %m월 %d일')

# 위키 URL 생성 (하이픈을 UTF-8 하이픈으로 대체)
wiki_date = datetime.today().strftime('%Y-%m-%d')
wiki_url = f'https://github.com/MRSND/study/wiki/{wiki_date.replace("-", "%E2%80%90")}'

today_date = f'[{today_date_str}]({wiki_url})\n\n'

# 기존 파일 내용을 읽어온다
with open(readme_file_path, "r") as file:
    lines = file.readlines()

# "## 스터디 일지" 이후에 새 날짜를 추가한다
new_content = []
found_study_log_section = False

for line in lines:
    new_content.append(line)
    if "## 스터디 일지" in line:
        found_study_log_section = True
    if found_study_log_section and not line.strip().startswith('['):
        new_content.append(today_date)
        found_study_log_section = False

# 새로운 내용을 파일에 쓴다
with open(readme_file_path, "w") as file:
    file.writelines(new_content)