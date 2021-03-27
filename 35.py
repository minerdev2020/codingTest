def solution(s):
    answer = []
    if len(s) < 5:
        return answer
    temp_list = []
    temp_attr = set()
    temp_str = ""
    check = False
    for i in s[1:-1]:
        if i == '}':
            check = False
            temp_attr.add(int(temp_str))
            temp_str = ""

            temp_list.append(temp_attr)
            temp_attr = set()
        elif i == '{':
            check = True
        elif i.isdigit():
            temp_str += i
        elif i == "," and check == True:
            temp_attr.add(int(temp_str))
            temp_str = ""

    temp_list.sort(key = lambda t:len(t))
    temp_set = copy.deepcopy(temp_list[0])
    answer.append(temp_set.pop())
    for i in range(1,len(temp_list)):
        answer.append((temp_list[i]-temp_list[i-1]).pop())
    return answer
