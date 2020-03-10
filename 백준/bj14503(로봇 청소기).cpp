//문제 - https://www.acmicpc.net/problem/14503
//내 코드 설명 - https://sohyunwriter.tistory.com/70
#include <iostream>
using namespace std;

#define MAX 51

int map[MAX][MAX];
int r, c, d;
int dx[4] = { -1, 0, 1, 0 }; //북 동 남 서
int dy[4] = { 0, 1, 0, -1 };

int bdx[4] = {1, 0, -1, 0}; //남 서 북 동
int bdy[4] = {0, -1, 0, 1};
int ans = 0;

void dfs(int r, int c, int d) {
	//벽이면 종료
	if (map[r][c] == 1)
		return;

	//청소한다
	if (map[r][c] == 0) {
		map[r][c] = 2;
		ans++;
	}

	//네 방향 체크
	for (int i = 0; i < 4; i++) {
		int nd = (d - 1 + 4) % 4;

		//새 위치
		int nx = r + dx[nd];
		int ny = c + dy[nd];

		if (map[nx][ny] == 0) {
			r = nx, c = ny, d = nd;
			dfs(r, c, d);
			return;
		}
		else {
			d = nd;
		}
	}

	//후진
	r = r + bdx[d], c = c + bdy[d];
	dfs(r, c, d);
}

int main() {
	int N, M; // 세로, 가로

	scanf("%d %d", &N, &M);

	scanf("%d %d %d", &r, &c, &d);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &map[i][j]);
		}
	}

	int change = 0;
	//search
	dfs(r, c, d);

	cout << ans;

	return 0;
}
