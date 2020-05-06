#include <iostream>
#include <vector>
#include <queue>
#include <cstdlib>
#define MAX 51
using namespace std;

int N, L, R;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };
int a[51][51];
int visited[51][51];
int ans = 0;

int main() {
	scanf("%d %d %d", &N, &L, &R);
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &a[i][j]);
		}
	}
	while (1) {
		int many = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (visited[i][j] == 1) {
					continue;
				}
				if (visited[i][j] == 0) {
					queue <pair <int, int> > q;
					queue <pair <int, int> > dq;
					int sum = a[i][j];

					q.push(make_pair(i, j));

					while (!q.empty()) {
						int x = q.front().first;
						int y = q.front().second;
						visited[x][y] = 1;
						q.pop();
						dq.push(make_pair(x, y));
						for (int k = 0; k < 4; k++) {
							int nx = x + dx[k];
							int ny = y + dy[k];
							if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
								if (visited[nx][ny] == 0) {
									int avail = abs(a[x][y] - a[nx][ny]);
									if (avail >= L && avail <= R) {
										visited[nx][ny] = 1;
										q.push(make_pair(nx, ny));
										sum += a[nx][ny];
									}
								}
							}
						}
					}//queue

					int count = dq.size();
					int now = sum / count;
					if (count == 1) {
						many++;
					}

					while (!dq.empty()) {
						int x = dq.front().first;
						int y = dq.front().second;
						a[x][y] = now;
						dq.pop();
					}
					sum = 0;

				}//if
			}
		}//for

		if (many == N * N) {
			break;
		}
		else {
			ans++;
		}

		//원복
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				visited[i][j] = 0;
			}
		}
	
	
	}
	
	cout << ans << endl;

	return 0;
}
