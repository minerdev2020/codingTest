# 해설 참조한 풀이
def to_seconds(time):
    temp = list(map(int, time.split(':')))
    return temp[0] * 3600 + temp[1] * 60 + temp[2]

def to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)

def solution(play_time, adv_time, logs):
    play_time_sec = to_seconds(play_time)
    adv_time_sec = to_seconds(adv_time)

    logs_start_sec = []
    logs_end_sec = []
    logs = list(map(lambda x: tuple(x.split('-')), logs))
    for log in logs:
        logs_start_sec.append(to_seconds(log[0]))
        logs_end_sec.append(to_seconds(log[1]))
        
    total_time = [0] * (play_time_sec + 1)
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1

    for i in range(1, play_time_sec):
        total_time[i] += total_time[i - 1]

    for i in range(1, play_time_sec):
        total_time[i] += total_time[i - 1]

    max_time = total_time[adv_time_sec - 1]
    answer = 0
    for i in range(adv_time_sec, play_time_sec):
        now_time = total_time[i] - total_time[i - adv_time_sec]
        if now_time > max_time:
            max_time = now_time
            answer = i - adv_time_sec + 1
                        
    return to_time(answer)