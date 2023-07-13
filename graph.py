"""
같은 그래프인지 판단
line의 개수가 1부터 최대까지 몇개의 점을 가지고 있는지 판단

조건
1. 점의 개수를 구함
2. 가장 높은 차수를 구함

판단
1. 점의 개수가 같은가?
2. 차수가 최대까지 갈 때 속한 점의 개수가 같은가?
"""

dot_max1 = int(input("첫번째 그래프의 점 개수를 입력하세요: "))
dot_max2 = int(input("두번째 그래프의 점 개수를 입력하세요: "))

line_max1 = int(input("첫번째 그래프의 최대 차수를 입력하세요: "))
line_max2 = int(input("두번째 그래프의 최대 차수를 입력하세요: "))

if (dot_max1 == dot_max2) and (line_max1 == line_max2):
    for line in range(1, line_max1+1):
        a = int(input(f"첫번째 그래프에서 차수가 {line}개인 점의 개수를 입력하세요: "))
        b = int(input(f"두번째 그래프에서 차수가 {line}개인 점의 개수를 입력하세요: "))
        if a == b: pass
        else:
            print("서로 다른 그래프입니다.")
    print("서로 같은 그래프입니다.")
else:
    print("서로 다른 그래프입니다.")
