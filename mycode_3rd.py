# 문제:  학생 10명의 성적을 입력받아 평균을 계산하는 코드로 작성하자 #문제상황
total = 0   # 변수 total의 초기값은 0이다.    #변수의 초기값을 설정하려면, 변수 이름과 초기값을 = 기호로 연결하여 선언
counter = 1 # 변수 counter의 값은 1이다.     #변수의 초기값을 설정하려면, 변수 이름과 초기값을 = 기호로 연결하여 선언
while counter <= 10: #반복문으로 counter의 값이 10이 될때까지 10번 돌면 종료한다. # 반복문을 사용, 변수의 값이 10이 될 때까지 반복문을 실행. 반복문 내부에서는 counter 변수의 값을 1씩 증가시키면서 반복문을 실행
    grade = int(input("성적을 입력하시오.:")) # 변수 grade는 정수형 변환문 int를 이용하여 입력받는다. #input() 함수를 사용하여 사용자로부터 입력을 받고, int() 함수를 사용하여 입력받은 문자열을 정수형으로 변환
    total = grade + total # 변수 grade의 값과 total의 값을 계산하여 다시 total에 선언(10번 증가)  #변수의 초기값을 설정하려면, 변수 이름과 초기값을 = 기호로 연결하여 선언
    counter = counter + 1 # 변수 counter의 값을 한번 시행시킬때마다 1씩 증가  #변수 counter의 값을 1 증가
average = total // 10 # 변수 average에 위 반복문에서의 결과값에 10으로 나눈다.  #변수 total의 값을 10으로 나눈 몫을 변수 average에 할당하는 코드
print(average) # 평균값을 출력  #print() 함수는 괄호 안에 있는 값을 출력하는 함수. average 변수를 출력하려면, print(average)와 같이 입력
# write by 김태경
