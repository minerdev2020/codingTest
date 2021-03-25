#include <vector>

using namespace std;

int find_size(int m, int n, int x, int y, int color, int n_size, vector<vector<int>> &picture) {
	if (x < 0 || y < 0 || x == m || y == n || picture[x][y] != color) {
		return n_size;
	}
	picture[x][y] = -1;
	n_size++;
	n_size = find_size(m, n, x+1, y, color, n_size, picture);
	n_size = find_size(m, n, x-1, y, color, n_size, picture);
	n_size = find_size(m, n, x, y+1, color, n_size, picture);
	n_size = find_size(m, n, x, y-1, color, n_size, picture);
	return n_size;
}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int number_of_area = 0;
	int max_size_of_one_area = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (picture[i][j] > 0) {
				number_of_area++;
				int size_of_one_area = find_size(m, n, i, j, picture[i][j], 0, picture);
				max_size_of_one_area = max(max_size_of_one_area, size_of_one_area);
			}
		}
	}
	vector<int> answer(2);
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}
