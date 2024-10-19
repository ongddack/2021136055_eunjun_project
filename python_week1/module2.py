from collections import Counter
import re

class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # 리스트의 연산: 클래스의 메소드
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e

def make_dictionary(lines):
    # 모든 단어를 추출하고 빈도수를 계산
    words = []
    for line in lines:
        # 특수문자를 제거하고 단어를 분리
        words += re.findall(r'\b\w+\b', line)
    # 단어의 빈도수 계산
    word_count = Counter(words)

    # 결과 출력
    for word, count in word_count.items():
        print(f"{word}: {count}")

    # 파일에 저장
    with open('dic.txt', 'w', encoding='utf-8') as f:
        for word, count in word_count.items():
            f.write(f"{word}: {count}\n")

# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)

while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-사전 만들기, q-종료=> ")

    if command == 'i':
        pos = int(input("  입력행 번호: "))
        str_input = input("  입력행 내용: ")
        list.insert(pos, str_input)

    elif command == 'd':
        pos = int(input("  삭제행 번호: "))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("  변경행 번호: "))
        str_input = input("  변경행 내용: ")
        list.delete(pos)  # 기존 내용을 삭제
        list.insert(pos, str_input)  # 새로운 내용 삽입

    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%2d] ' % line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q':
        exit()

    elif command == 'l':
        filename = 'test.txt'
        with open(filename, "r", encoding='utf-8') as infile:
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size, line.rstrip('\n'))

    elif command == 's':
        filename = 'test.txt'
        with open(filename, "w", encoding='utf-8') as outfile:
            len_lines = list.size
            for i in range(len_lines):
                outfile.write(list.getEntry(i) + '\n')

    elif command == 'm':
        # 사전 만들기
        lines = [list.getEntry(i) for i in range(list.size)]
        make_dictionary(lines)
