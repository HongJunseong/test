#입력한 ID를 조건에 맞게 만들어주는 코드
#특수문자를 포함한 문자열을 파라미터로 입력하면 특정 특수문자를 제외한 나머지 특수문자들을 제거해줌
#..는 2번이상 반복될 수 없고, 양 끝은 .이 될 수 없다
#정규표현식(re)를 
import re

def solution(new_id):

    answer = ''

    beflen = len(new_id)
    
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z\-\_\.]', "", new_id) #특수문자 제거
    new_id = re.sub('[.]{2,}',".", new_id) #.가 2번이상 반복되면 제거
    new_id = new_id.strip('.') #양 끝 .제거
    
    if new_id == '':
        new_id = "{}".format('a') #위의 과정을 거쳤을 때 new_id가 빈 문자열이면 a로 채움
        
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = new_id.rstrip('.') #new_id의 길이 제한
        
    if len(new_id) <= 2:
        if len(new_id) == 1:
            new_id = new_id + new_id[0] * 2
        elif len(new_id) == 2:
            new_id = new_id + new_id[1]
        
    answer = answer + new_id
    return answer

print(solution("#!@#Jun!seon@*g#."))
#특수 문자들이 제거되며 junseong이 출력됨
