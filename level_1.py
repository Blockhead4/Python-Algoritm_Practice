# 1. 문자열 다루기 기본
# alpha_string46함수는 문자열 s를 매개변수로 입력받습니다. 
# s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요. 
# 예를들어 s가 “a234”이면 False를 리턴하고 “1234”라면 True를 리턴하면 됩니다
import re
def alpha_string46(s) :
    if (len(s) == 4 or len(s) ==  6) and not re.findall(r"[A-Za-z]",s):
        print(s)

s = "123456"

alpha_string46(s)

    

#