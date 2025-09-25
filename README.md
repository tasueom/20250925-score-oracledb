# 20250925-score-oracledb

SQLite 기반 예제를 Oracle DB 연동으로 변환하여 CRUD 동작을 학습하는 간단한 연습 프로젝트

## 개발 기능 정리

### 초기 환경 세팅
- Flask 애플리케이션 생성
- 최초 실행 시 students테이블 student_seq 시퀀스 자동 생성

### 성적 관리

- 성적 입력: 이름과 국어, 영어, 수학 점수 입력받아 저장 후 총점, 평균, 학점 계산하여 자동부여되는 학번과 함께 DB에 저장
- 성적 수정: 이름, 국어, 영어, 수학 수정 가능. 총점, 평균, 학점은 자동으로 재계산
- 성적 삭제: 리스트 화면에서 특정 성적의 삭제 버튼 클릭 시 해당 성적 제거

### 실행 방법

- 의존성 설치
```bash
pip install flask oracledb
```
- 파일 준비
Oracle Instant Client (Windows x64) 다운로드:
https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
C:\oraclexe 경로에 압축 해제
- 서버 실행: python app.py
- 접속 주소: http://127.0.0.1:5000