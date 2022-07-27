#----------------------------------------------------------------------------
# 문자열 데이터 타입(str) 살펴보기
#----------------------------------------------------------------------------
# 컴퓨터 메모리에 문장열 데이터 저장
msg='helloo'

# 1번요소 읽어와서 출력
print(msg[1])

# 1번요소에 값을 E로 변경
# msg[1]='E' ---------------------> str타입(문자열)은 요소값을 변결할 수 없다.(문자열=immutable한 자료형)
msg2=msg[0]+'E'+msg[2:]
#   'H' +  +'E'+'lloo'
print(msg,msg2)


#---------------------------- 문자열 포맷팅(양식, Formatting)----------------------------------------
# 문법 => A= " %알파벳 " %삽입할 값
#        A= ' %알파벳 ' %삽입할 값
# 문장 뒤에 %삽입할 값이 오지 않으면 문자열 포맷팅 기능은 동작하지 않는다.
#------------------------------------------------------------------------------------------------

weather= "현재 온도는 29도 입니다."
print(weather)

temp=32
weather= "현재 온도는 %d도 입니다." %temp
print(weather)

#변수만 바꿔서 문장에 적용하기
#이렇게 하면 12 적용안됨.
temp=12
print(weather)
#함수를 쓰지 않으면 문장을 가져와야 함.
temp=12
print("현재 온도는 %d도 입니다." %temp)
temp=-4

#------------------------------문자열 포맷 코드--------------------------------------------------------------

print("현재 온도는 %d도 입니다." %temp) #정수 => %d
temp=-4
print("현재 온도는 %f도 입니다." %temp) #실수 => %f
temp=-4
print("현재 온도는 %s도 입니다." %temp) #문자열 => %s
temp="a"
print("현재 온도는 %c도 입니다." %temp) #문자1개 => %c
temp=-4
print("현재 온도는 %d%% 입니다." %temp) # %자체 => %%

# --------------------------한 문장에 포맷팅을 코드를 여러개 사용할 때 사용법-----------------------------------
# 생년월일을 문자열 포맷팅으로 만들기

year=2000
month=3
day=12
birth="나의 생일은 %d년 %d월 %d일 입니다." %(year, month, day) #-----> 괄호 열고 갯수만큼 쉼표로 나열 후 괄호 닫기.
print(birth)

#------------------------------------- 정렬과 공백 ---------------------------------------------------------
# "%숫자s" %a -> %s 사이에 숫자 넣기
print(("%10s") %'Good') #-------------------------------->오른쪽 정렬
print(("%-10s") %'Good')#-------------------------------->왼쪽 정렬
print(("%-10s") %'Merry Christmas')
print(("%10s") %'Merry Christmas') #----------------------->10칸인데 문자가 10개를 초과하면 의미 없음.
print(("%100s") %'Merry Christmas')
print(("%100sjane") %'Merry Christmas')
print(("%-100sjane") %'Merry Christmas')

#-----------------------------------문자 데이터 타입 전용의 함수 사용 ex) .format()------------------------------------------
# str전용 함수를 method함수(m)라고 부른다.
# 문자열.함수명() or 문자열변수.함수명() , 함수명=> 메서드  ex) "a".format()
# str전용 함수 사용법: "a". ---------->점찍어주면됨.
# format 함수 사용법: "{} ".format()

"나의 이름은 {}이고 별명은 {}입니다".format("마징가", "베트맨")

msg="오늘은 {}년 {}월 {} 입니다".format(2022,5,19) #---> 괄호 안 번호 생략가능 (가만히 두면 괄호 순서대로 0,1,2순서로 진행)
msg2="오늘은 {1}년 {0}월 {2} 입니다".format(2022,5,19) #---> 괄호 안 번호를 지정해 줄 수 있음.
print(msg)
print(msg2)

#------------------------------------함수 정렬-----------------------------------------------------------
# :>10 : 오른쪽 정렬
# :<10 : 왼쪽 정렬
# :^10 : 가운데 정렬
#공백은 채우고 싶으면 , <>^ 앞에 채울 기호 넣으면 됨 "{0:!^10}".format("hi")
#-----------------------------------f 문자열 포매팅----------------------------------------------------------
# f' {데이터 또는 변수명} ' 또는 f" {데이터 또는 변수명} "
# f---> format 약자

num1=10
num2=3
print("10+2= ",num1+num2)  #-----> num 이 바뀌면 10+2 문자열도 바꿔야하면 귀찮음. ----> f문자열 포매팅 사용하면 됨.
print(f"{num1}+{num2}={num1+num2}")