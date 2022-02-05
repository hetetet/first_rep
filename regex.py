import re

p=re.compile("ca.e")

m=p.match("careless")
def print_match(m):
    if m:
        print(m.group()) #일치하는 문자열 반환
        print(m.string) #입력받은 문자열 그대로 출력
        print(m.start()) #일치하는 문자열의 시작 인덱스
        print(m.end()) #일치하는 문자열의 끝 인덱스
        print(m.span()) #일치하는 인덱스의 시작과 끝을 함께 표시
    else:
        print("매칭되지 않음")
        
print_match(m)

m=p.match("careless")#주어진 문자열의 처음부터 일치하는지 확인해서 이것도 맞다 한다

lst=p.findall("good care cafe")
print(lst)

#1.p=re.compile("원하는 형태")
#2.m=p.match("비교할 문자열"): 주어진 문자열의 처음부터 일치하는지 확인
#3.m=p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
#4. lst=p.findall("비교할 문자열"): 일치하는 모든 것을 리스트 형태로 반환

# .(ca.e) 하나의 문자를 의미 > care, cafe, cave (o) | caffe(x)
# ^(^de) 문자열의 시작 > desk, demon(o) | fade(x)
#$(se$) 문자열의 끝 > case, diverse(o) | sea(x)