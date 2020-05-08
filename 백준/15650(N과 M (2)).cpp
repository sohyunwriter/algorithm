#include <iostream>
#include <vector>
using namespace std;

vector <int> ans;
int N, M;

void dfs(int idx) {
	if (ans.size() == M) { //탈출 조건
		for (auto i : ans)
			cout << i << " ";
		cout << endl;
		return;
	}

	for (int i = idx; i <= N; i++) { //탐색
		if (ans.size() < M) {
			ans.push_back(i); //넣고
			dfs(i + 1); //dfs 재귀(i 다음 값을 이전의 값 또 탐색하지 않도록 함)
			ans.pop_back(); //빼고
		}
	}
}

int main() {
	scanf("%d %d", &N, &M);
	dfs(1);

	return 0;
}
