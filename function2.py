# 스코핑룰(이름 해석 규칙):LGB 규칙
x = 1
def func(a):
    return a+x
# 호출
print(func(1))

def func2(a):
    x = 5
    return a+x

# 호출
print(func2(1))
