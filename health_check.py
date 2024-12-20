from flask import Flask, jsonify
import subprocess
import requests

app = Flask(__name__)

def check_process(process_name):
    """
    주어진 프로세스 이름이 실행 중인지 확인.
    :param process_name: 확인할 프로세스 이름
    :return: 실행 중이면 True, 아니면 False
    """
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        return process_name in result.stdout
    except Exception as e:
        return False

def report_status(server_url, status):
    """
    상태를 외부 서버에 보고.
    :param server_url: 상태를 보고할 서버 URL
    :param status: 프로세스 상태 ('running' 또는 'stopped')
    """
    try:
        response = requests.post(server_url, json={"status": status})
        return response.status_code
    except Exception as e:
        return str(e)

@app.route('/health-check', methods=['GET'])
def health_check():
    """
    헬스 체크 API 엔드포인트
    """
    process_name = "tail"  # 확인할 프로세스 이름
    server_url = "http://your-server-url.com/report"  # 상태 보고 URL

    is_running = check_process(process_name)
    status = "running" if is_running else "stopped"
    report_code = report_status(server_url, status)

    return jsonify({
        "process_name": process_name,
        "status": status,
        "report_status": report_code
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
