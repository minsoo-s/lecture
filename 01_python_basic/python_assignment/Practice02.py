# -----------------------------------------------------------
# [숫자와 문자열 자료형 이해 220518]
#1. 숫자 자료형(int, float)을 다루는 문제입니다.
#형식 : 변수명=데이터
#1-1. 숫자 45.98을 컴퓨터 메모리에 저장해 주세요.
#1-2. 오늘의 년도, 월, 일을 컴퓨터 메모리에 저장해 주세요.
#1-3. 키와 몸무게를 컴퓨터 메모리에 저장해 주세요.
#1-4. 국사, 과학, 미술 점수를 컴퓨터 메모리에 저장해 주세요.
#1-5. 숫자를 계산하는 4칙 연산과 몫, 나머지를 구하는 연산을 수행하기 위한 기호 즉 연산자를 적어주세요.
#1-6. 숫자 2개 5와 3을 사용해서 연산 수행 후 결과를 화면에 보여주세요.
#(4칙 연산과 몫, 나머지 연산으로 6가지 연산 결과 출력)

numbers=float(45.98)
year=int(2022)
month=int(5)
day=int(19)
height=int(179)
weight=int(81)
국사점수=int(80)
과학점수=int(100)
미술점수=int(90)
덧셈=5+3
뺄셈=5-3
곱셈=5*3
나눗셈=5/3
몫=5//3
나머지=5%3

print("덧셈(5+3): ",덧셈)
print("뺄셈(5-3): ",뺄셈)
print("곱셈(5*3): ",곱셈)
print("나눗셈(5/3): ",나눗셈)
print("몫연산(5//3): ",몫)
print("나머지 연산(5%3): ", 나머지)
#--------------------------------------------------------------
#2. 문자열(String)을 다루는 문자열 자료형(str)을 다루는 문제입니다.
#형식 : 변수명=데이터
#2-1. 새해 인사를 컴퓨터 메모리에 저장해 주세요.
#(예: 새해 복 많이 많이 받으세요.)
#2-2. 나의 생일을 컴퓨터 메모리에 저장해 주세요.
#(예: 2022년 1월 15일)
#2-3. 전화번호를 컴퓨터 메모리에 저장해 주세요.
#(예: 010-2222-1212)
#2.4 문자열 자료형을 이해하기 위해서 아래 설명에 해당하는 용어를 넣어주세요.
#2-5. 나의 생일, 전화번호 문자열 데이터에서 일부만 출력해주세요.
#- 나의 생일 데이터 => 월만 출력

#- 전화번호 데이터 => 010, 2222, 1212를 각각 따로 따로 출력
#- 전화번호 처음부터 끝까지 출력
#2-6. ‘ ’, “ ” 사이에서 특별한 의미를 가지는 문자는 무엇인가요?
#2-7. 다음 문자의 의미는 무엇인가요?
#‘오늘은\n토요일입니다.’ => 출력 결과
#‘C\User\my\Download’ => 출력 결과 오류 발생, 수정해주세요.

새해인사="새해 복 많이 많이 받으세요."
나의생일="1994년 7월 7일"
전화번호="010-9594-6754"
#2.4 (A) 자료형, 인덱스, 슬라이싱
print("나의 생일: ",나의생일[6:8])
print("전화번호 일부: ",전화번호[:3],전화번호[4:8],전화번호[9:])
print("전화번호 끝까지: ", 전화번호[:])
#2.6 (A)\
print('오늘은\n토요일입니다.')
#2.7 (A)줄바꿈
print('C\\User\\my\\Download')
print(r'C\User\my\Download')
#------------------------------------------------------------------------------------
#3. 다음 중 잘못 된 부분이 있다면 이유를 설명해 주세요.
#3-1. 1_number = 12
#3-2. my id = ‘stdID’
#3-3. _phone=’010’
#3-4. myID=’no0001’
#3-5. name=“”“
#Happy
#New
#year“”“

#3-1 (A)변수 제일 앞 글자 숫자 안됨.
#3-2 (A)변수 띄어쓰기 안됨.
#3-3.(A)가능.
#3-4 (A)가능.
#3-5 (A)가능.

#--------------------------------------------------------------------------------------
#4. 다음 문제에 답해주세요~.
#4-1. 숫자형 데이터를 문자형 데이터로 변환하는 것은 무엇인가요?
#4-2. 변환해 주세요~
#“123.45”를 실수로 변환해 주세요.
#“No123”을 정수로 변환해 주세요.
#2022를 문자열로 변환해 주세요.
#19.20을 문자열로 변환해 주세요.

#4-1.(A) 형변환(타입 캐스팅), str(), ""
#4-2.(A)
print(float("123.45"))
# 정수로 변화 불가능, "No123"
str(2022)
str(19.20)