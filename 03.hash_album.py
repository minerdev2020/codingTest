def solution(genres, plays):
    answer = []
    genres_table = {}
    songs_table = {}

    for i, genre in enumerate(genres):
        if genre not in genres_table:
            genres_table[genre] = plays[i];
            songs_table[genre] = [(i, plays[i])]

        else:    
            genres_table[genre] += plays[i]
            songs_table[genre].append((i, plays[i]))

    for key, value in songs_table.items():
        value = sorted(value, key=lambda item: item[1], reverse=True)
        songs_table[key] = value

    genres_rank = sorted(genres_table.items(), key=lambda item: item[1], reverse=True)

    for item in genres_rank:
        answer.append(songs_table[item[0]][0][0])

        if len(songs_table[item[0]]) > 1:
            answer.append(songs_table[item[0]][1][0])

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop', 'k-pop'], [500, 600, 150, 800, 2500, 9000]))