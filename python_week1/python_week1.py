import time

# 하노이 타워 함수
def hanoi_tower(n, fr, tmp, to):
    global count  # 호출 횟수를 세기 위한 전역 변수
    if n == 1:
        count += 1
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        count += 1
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)

# 테스트 프로그램
n = int(input("하노이 타워의 최대 층 수를 입력하세요: "))
count = 0  # 호출 횟수 초기화

start = time.time()  # 시작 시간

hanoi_tower(n, 'A', 'B', 'C')  # 하노이 타워 함수 호출

end = time.time()  # 종료 시간

print("하노이 타워 함수 호출 횟수:", count)
print("실행 시간 = ", end - start)

