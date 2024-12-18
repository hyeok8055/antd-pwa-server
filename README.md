# antd-pwa-server-db

## 소개
FastAPI와 MongoDB를 기반으로 한 백엔드 서버입니다. 사용자 인증(일반 로그인 및 카카오 소셜 로그인)을 지원합니다.

## 주요 기능
- 회원 관리
  - 일반 회원가입/로그인
  - 카카오 소셜 로그인
  - 로그아웃
- 사용자 인증
  - JWT 기반 토큰 인증
  - 소셜 로그인 연동

## 기술 스택
- FastAPI
- MongoDB (with Motor)
- JWT (JSON Web Tokens)
- Pydantic
- Python 3.8+

## 설치 방법

1. 가상 환경 생성 및 활성화 (선택 사항이지만 권장)
```bash
# 가상 환경 생성 (venv 사용 예시)
python3 -m venv .venv

# 가상 환경 활성화
source .venv/bin/activate
```

2. 의존성 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정
```bash
# .env 파일 생성
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=mydatabase
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
KAKAO_CLIENT_ID=your-kakao-client-id
KAKAO_CLIENT_SECRET=your-kakao-client-secret
```

4. 서버 실행
```bash
uvicorn fastapi.main:app --reload
```

## API 엔드포인트

### 인증 관련
- `POST /auth/register`: 새 사용자 등록
- `POST /auth/login`: 로그인
- `POST /auth/logout`: 로그아웃
- `GET /auth/kakao/login`: 카카오 로그인 시작
- `GET /auth/kakao/callback`: 카카오 로그인 콜백

### 사용자 관련
- `GET /users/me`: 현재 로그인한 사용자 정보 조회
- `PUT /users/me`: 사용자 정보 수정

## 데이터 모델

### User 모델
- `email`: 이메일 (고유값)
- `username`: 사용자 이름
- `hashed_password`: 해시된 비밀번호
- `is_active`: 계정 활성화 상태
- `is_social`: 소셜 계정 여부
- `social_provider`: 소셜 로그인 제공자 (예: "kakao")
- `social_id`: 소셜 서비스의 사용자 ID
- `created_at`: 계정 생성 시간
- `last_login`: 마지막 로그인 시간

## 보안
- 비밀번호는 bcrypt로 해시하여 저장
- JWT를 사용한 토큰 기반 인증
- CORS 미들웨어 설정

## 향후 개선사항
- [ ] 이메일 인증 추가
- [ ] 비밀번호 재설정 기능
- [ ] 추가 소셜 로그인 (구글, 네이버 등)
- [ ] 리프레시 토큰 구현
- [ ] API 문서화 개선

