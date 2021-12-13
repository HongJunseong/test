import re

def solution(new_id):

    answer = ''

    beflen = len(new_id)
    
    new_id = new_id.lower()
    
    new_id = re.sub('[!@#$%^&*(:~)+>\`<}{\|\'\[\]\",/\=]', "", new_id) #특수문자 제거
    
    new_id = re.sub('[.]{2,}',".", new_id) #.가 2번이상 반복되면 제거
    
    new_id = new_id.strip('.') #양 끝 .제거
    
    if new_id == '':
        new_id = "{}".format('a' * beflen) #빈 문자열을 처음 new_id의 길이만큼 a로 채움
        
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = new_id.rstrip('.')
        
    if len(new_id) <= 2:
        if len(new_id) == 1:
            new_id = new_id + new_id[0] * 2
        elif len(new_id) == 2:
            new_id = new_id + new_id[1]
        
    answer = answer + new_id
    return answer
