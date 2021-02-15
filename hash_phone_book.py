# 내 풀이
def solution(phone_book):
    for phone in phone_book:
        for other_phone in phone_book:
            if len(phone) >= len(other_phone):
                continue

            if hash(phone) == hash(other_phone[:len(phone)]):
                return False

    return True

# 다른 사람의 풀이
def solution1(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            if temp in hash_map and temp != phone_number:
                return False

    return True

def solution2(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))