vector<vector<int>> Rotate(vector<vector<int>> matrix) {
	vector<vector<int>> result(matrix);
	for (int i = 0; i < matrix.size(); i++) {
		for (int j = 0; j < matrix.size(); j++) {
			result[i][j] = matrix[j][matrix.size() - i - 1];
		}
	}
	return result;
}


bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int N = key.size();
    int M = lock.size();
    vector<vector<int>> paper(M + (N - 1) * 2, vector<int>(M + (N - 1) * 2, 0));
    int size = N + M - 1;
    for (int i = N - 1; i < size; i++)
        for (int j = N - 1; j < size; j++)
            paper[i][j] = lock[i - (N - 1)][j - (N - 1)];
    for (int rot = 0; rot < 4; rot++) {
        key = Rotate(key);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                vector<vector<int>> tmp(paper);
                for (int x = 0; x < N; x++) {
                    for (int y = 0; y < N; y++) {
                        tmp[i + x][j + y] += key[x][y];
                    }
                }
                int flag = 0;
                for (int x = N - 1; x < size; x++) {
                    for (int y = N - 1; y < size; y++) {
                        if (tmp[x][y] != 1) {
                            flag = 1;
                            break;
                        }
                    }
                    if (flag) break;
                }
                if (!flag) return true;
            }
        }
    }
    return false;
}
