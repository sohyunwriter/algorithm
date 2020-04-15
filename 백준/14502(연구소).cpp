//https://sohyunwriter.tistory.com/144

#include <iostream>
#include <queue>
#define MAX 9
using namespace std;

int n, m; //세로(행), 가로(열)
int lab[MAX][MAX];
int wboard[MAX][MAX];
int ans = 0;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };

void bfs(void) { //바이러스 퍼트리기
	int vboard[MAX][MAX];
	int safecnt = 0;
	
	//wboard -> vboard
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			vboard[i][j] = wboard[i][j];
		}
	}

	//바이러스 퍼트리기
	queue<pair <int, int> > q;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (vboard[i][j] == 2) {
				q.push(make_pair(i, j));

				while (!q.empty()) {
					int x = q.front().first;
					int y = q.front().second;
					q.pop();

					for (int k = 0; k < 4; k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];
						if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
							if (vboard[nx][ny] == 0) {
								vboard[nx][ny] = 2;
								q.push(make_pair(nx, ny));
							}
						}
					}
				}

			}
		}
	}

	//바이러스 퍼진 후 0인 공간 세기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (vboard[i][j] == 0) {
				safecnt++;
			}
		}
	}

	//0인 개수가 현재 ans보다 많으면 ans 갱신
	if (safecnt > ans) {
		ans = safecnt;
	}

}

void makeWall(int count) { // 벽 3개 세우기
	if (count == 3) {
		bfs();
		return;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (wboard[i][j] == 0) {
				wboard[i][j] = 1;
				makeWall(count + 1);
				wboard[i][j] = 0;
			}
		}
	}
}

int main() {	
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &lab[i][j]);
			wboard[i][j] = lab[i][j];
		}
	}

	//makewall
	//처음 지점을 잡기 위해 처음 지점 잡고 makeWall(1)
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lab[i][j] == 0) {
				wboard[i][j] = 1;
				makeWall(1);
				wboard[i][j] = 0;
			}
		}
	}

	cout << ans << endl;

	return 0;
}
