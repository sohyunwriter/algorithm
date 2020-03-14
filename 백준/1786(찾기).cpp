#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

vector<int> getPi(string p) {
	int m = p.size(), j = 0;
	vector<int> pi(m, 0); // 0으로 초기화
	for (int i = 1; i < m; i++) {
		while (j > 0 && p[i] != p[j])
			j = pi[j - 1];
		if (p[i] == p[j])
			pi[i] = ++j;
	}
	return pi;
}

vector<int> kmp(string t, string p) {
	vector<int> ans;
	auto pi = getPi(p);
	int n = t.size(), m = p.size(), j = 0;
	for (int i = 0; i < n; i++) {
		while (j > 0 && t[i] != p[j])
			j = pi[j - 1];
		if (t[i] == p[j]) {
			if (j == m - 1) {
				ans.push_back(i-m+1);
				j = pi[j];
			}
			else {
				j++;
			}
		}
	}
	return ans;
}

int main() {	
	string T, P;
	getline(cin, T);
	getline(cin, P);
	auto ans = kmp(T, P);
	cout << ans.size() << "\n";
	for (const auto& element : ans) //const 쓰는 게 좋음
		cout << (element + 1) << ' '; //0부터 계산했으므로
	return 0;
}
