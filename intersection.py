a = int(input())
en = set(map(int, input().split()))

b = int(input())
fr = set(map(int, input().split()))

print(len(en.intersection(fr)))