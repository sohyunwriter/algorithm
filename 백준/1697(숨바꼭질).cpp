#include <iostream>
#include <queue>

using namespace std;

//bfs
int bfs(int n, int k) {
	int visit[100001] = {0};
	queue<int> q;
	q.push(n);
	visit[n] = 1;

	while (!q.empty()) {
		int cn = q.front();
		q.pop();

		if (cn == k)
			return visit[cn]-1;

		if (cn +1 >= 0 && cn +1 <= 100000 && visit[cn + 1] == 0) {
			q.push(cn + 1);
			visit[cn + 1] = visit[cn] + 1; //dp를 이용하면 make_pair 안 해도 됨
		}

		if (cn - 1 >= 0 && cn - 1 <= 100000 && visit[cn - 1] == 0) {
			q.push(cn - 1);
			visit[cn - 1] = visit[cn] + 1;
		}

		if (cn * 2 >= 0 && cn * 2 <= 100000 && visit[cn*2] == 0) {
			q.push(cn*2);
			visit[cn * 2] = visit[cn] + 1;
		
		}

	}
}

int main() {
	int N, K;
	int ans;
	scanf("%d %d", &N, &K);

	ans = bfs(N, K);
	cout << ans;

	return 0;
}
