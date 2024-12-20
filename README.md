


- 가상환경 실행
```sh
.\venv\Scripts\activate
```

- 도커 파일 빌드
```sh
docker build -t health-check .
```

- 도커에 health-check 5000번 포트로 올리기
```sh
docker run --name health-check-container -p 5000:5000 health-check
```

- 도커 컨테이너에 들어가기
```sh
docker exec -it <container-name> bash
```


