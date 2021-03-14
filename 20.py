import re

def solution(new_id):
    result = new_id.lower()
    result = re.sub('[^a-z0-9\-_.]', '', result)
    result = re.sub('[.]+', '.', result)
    result = re.sub('^[.]|[.]$', '', result)
    result = 'a' if len(result) == 0 else result[:15]
    result = re.sub('^[.]|[.]$', '', result)
    while len(result) < 3 :
       result += result[-1]
      
    return result
