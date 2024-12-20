FROM python:3.9-slim

# 시스템 패키지 설치
RUN apt update && apt install -y python3 python3-pip python3-venv

# 가상 환경 생성 및 활성화
RUN python3 -m venv /app/venv

# 가상 환경에 패키지 설치
COPY requirements.txt requirements.txt
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# 작업 디렉토리 설정
WORKDIR /app
COPY . .

# 가상 환경에서 실행
CMD ["/app/venv/bin/python", "health_check.py"]
