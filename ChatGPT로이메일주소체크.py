import re

# 이메일 정규 표현식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 이메일 유효성 검사 함수
def is_valid_email(email):
    return re.match(email_pattern, email) is not None

# 테스트할 이메일 샘플 10개 (유효한 것과 유효하지 않은 것 섞음)
email_samples = [
    "user@example.com",           # 유효
    "john.doe@sub.domain.co",     # 유효
    "user123@domain",             # ❌ (도메인 끝이 없음)
    "user.name+tag@domain.org",   # 유효
    "user@.com",                  # ❌ (도메인 앞이 없음)
    "user@domain.c",              # ❌ (최상위 도메인이 너무 짧음)
    "user@domain.company",        # 유효
    "invalid-email@",             # ❌ (도메인 없음)
    "just_text_without_at",       # ❌
    "user_name@domain.net"        # 유효
]

# 검사 실행
for email in email_samples:
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email:30} → {result}")


import re  # 정규표현식을 사용하기 위해 re 모듈을 불러옵니다

# 이메일 형식을 검사할 정규표현식 패턴
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# 설명:
# ^                  → 문자열의 시작
# [a-zA-Z0-9._%+-]+  → 영어 대소문자, 숫자, 점(.), 밑줄(_), 퍼센트(%), 더하기(+), 빼기(-)를 하나 이상 포함
# @                  → 반드시 @ 기호가 있어야 함
# [a-zA-Z0-9.-]+     → 영어 대소문자, 숫자, 점(.), 빼기(-)를 하나 이상 포함 (도메인 이름 부분)
# \.                 → 진짜 점(.) 하나
# [a-zA-Z]{2,}       → 영어 글자 2개 이상 (com, net, org 같은 최상위 도메인)
# $                  → 문자열의 끝

# 이메일 유효성 검사 함수 정의
def is_valid_email(email):
    # re.match 함수를 사용해서 이메일이 위의 패턴과 맞는지 확인
    return re.match(email_pattern, email) is not None

# 테스트용 이메일 샘플 리스트 (10개)
email_samples = [
    "user@example.com",           # 올바른 이메일
    "john.doe@sub.domain.co",     # 올바른 이메일 (하위 도메인 포함)
    "user123@domain",             # 잘못된 이메일 (도메인 끝 부분이 없음)
    "user.name+tag@domain.org",   # 올바른 이메일 (+ 기호 허용됨)
    "user@.com",                  # 잘못된 이메일 (도메인 이름 없음)
    "user@domain.c",              # 잘못된 이메일 (도메인 끝이 한 글자)
    "user@domain.company",        # 올바른 이메일 (긴 도메인도 허용됨)
    "invalid-email@",             # 잘못된 이메일 (@ 뒤가 없음)
    "just_text_without_at",       # 잘못된 이메일 (@ 기호가 없음)
    "user_name@domain.net"        # 올바른 이메일 (밑줄 포함)
]

# 각 이메일을 검사해서 결과 출력
for email in email_samples:
    # is_valid_email 함수로 검사한 결과에 따라 출력 메시지 결정
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email:30} → {result}")
