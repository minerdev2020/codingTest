from collections import deque

def count_area_by_bfs(m, n, s, picture):
    height = m
    width = n
    color = picture[s[0]][s[1]]
    picture[s[0]][s[1]] = 0

    queue = deque()
    queue.append(s)
    count = 0
    while queue:
        cursor = queue.popleft()
        
        if cursor[0] + 1 < height and color == picture[cursor[0] + 1][cursor[1]]:
            queue.append([cursor[0] + 1, cursor[1]])
            picture[cursor[0] + 1][cursor[1]] = 0
            
        if cursor[1] + 1 < width and color == picture[cursor[0]][cursor[1] + 1]:
            queue.append([cursor[0], cursor[1] + 1])
            picture[cursor[0]][cursor[1] + 1] = 0
            
        if cursor[0] - 1 >= 0 and color == picture[cursor[0] - 1][cursor[1]]:
            queue.append([cursor[0] - 1, cursor[1]])
            picture[cursor[0] - 1][cursor[1]] = 0
            
        if cursor[1] - 1 >= 0 and color == picture[cursor[0]][cursor[1] - 1]:
            queue.append([cursor[0], cursor[1] - 1])
            picture[cursor[0]][cursor[1] - 1] = 0
            
        count += 1
        
    return count

def solution(m, n, picture):
    numberOfArea = 0
    maxSizeOfOneArea = 0
    
    for y, row in enumerate(picture):
        for x, col in enumerate(row):
            if col != 0:
                area = count_area_by_bfs(m, n, [y, x], picture)
                numberOfArea += 1
                maxSizeOfOneArea = max(maxSizeOfOneArea, area)

    answer = [numberOfArea, maxSizeOfOneArea]
    return answer

print(solution(6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], 
                      [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))
print(solution(6, 4, [[1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1],
                      [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]))
print(solution(6, 4, [[1, 1, 1, 0], 
                      [0, 0, 0, 1], 
                      [0, 0, 1, 0],
                      [0, 1, 0, 0], 
                      [0, 0, 0, 0], 
                      [0, 0, 0, 0]]))
print(solution(2, 2, [[1, 1], 
                      [1, 1]]))
print(solution(1, 1, [[0]]))
print(solution(13, 16, [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
                        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
                        [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0], 
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
                        [0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 0], 
                        [0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0], 
                        [0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]))


# JAVA 버전
# import java.util.LinkedList;
# import java.util.Queue;

# class Solution {
#     public int[] solution(int m, int n, int[][] picture) {
#         int numberOfArea = 0;
#         int maxSizeOfOneArea = 0;
#         int[] answer = new int[2];

#         int height = m;
#         int width = n;
#         int[][] myPicture = new int[height][width];
#         for (int y = 0; y < height; y++) {
#             for (int x = 0; x < width; x++) {
#                 myPicture[y][x] = picture[y][x];
#             }
#         }

#         for (int y = 0; y < height; y++) {
#             for (int x = 0; x < width; x++) {
#                 if (myPicture[y][x] != 0) {
#                     int area = countAreaByBfs(height, width, new Integer[]{y, x}, myPicture);
#                     maxSizeOfOneArea = maxSizeOfOneArea < area ? area : maxSizeOfOneArea;
#                     numberOfArea++;
#                 }
#             }
#         }

#         answer[0] = numberOfArea;
#         answer[1] = maxSizeOfOneArea;
#         return answer;
#     }

#     public int countAreaByBfs(int height, int width, Integer[] s, int[][] picture) {
#         int color = picture[s[0]][s[1]];
#         picture[s[0]][s[1]] = 0;
            
#         Queue<Integer[]> queue = new LinkedList<>();
#         queue.add(s);

#         int count = 0;
#         while (!queue.isEmpty()) {
#             Integer[] cursor = queue.poll();
#             picture[cursor[0]][cursor[1]] = 0;

#             if (cursor[0] + 1 < height && color == picture[cursor[0] + 1][cursor[1]]) {
#                 queue.add(new Integer[]{cursor[0] + 1, cursor[1]});
#                 picture[cursor[0] + 1][cursor[1]] = 0;
#             }

#             if (cursor[1] + 1 < width && color == picture[cursor[0]][cursor[1] + 1]) {
#                 queue.add(new Integer[]{cursor[0], cursor[1] + 1});
#                 picture[cursor[0]][cursor[1] + 1] = 0;
#             }

#             if (cursor[0] - 1 >= 0 && color == picture[cursor[0] - 1][cursor[1]]) {
#                 queue.add(new Integer[]{cursor[0] - 1, cursor[1]});
#                 picture[cursor[0] - 1][cursor[1]] = 0;
#             }

#             if (cursor[1] - 1 >= 0 && color == picture[cursor[0]][cursor[1] - 1]) {
#                 queue.add(new Integer[]{cursor[0], cursor[1] - 1});
#                 picture[cursor[0]][cursor[1] - 1] = 0;
#             }

#             count += 1;
#         }

#         return count;
#     }
# }