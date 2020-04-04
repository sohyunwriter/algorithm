//문제 - https://www.acmicpc.net/problem/5582
//내 코드 설명 - https://sohyunwriter.tistory.com/73
#include <iostream>
#include <string>
using namespace std;

#define MAX 4001

int main() {
	string s1, s2;
	int dp[MAX][MAX];
	int ans = 0; // 빈 문자열

	cin >> s1;
	cin >> s2;

	for (int i = 0; i < s1.length(); i++) {
		for (int j = 0; j < s2.length(); j++) {
			if (s1.at(i) != s2.at(j)) {
				dp[i][j] = 0;
			}
			else {
				dp[i][j] = dp[i - 1][j - 1] + 1;
				if (dp[i][j] > ans)
					ans = dp[i][j];
			}

		}
	}

	cout << ans;

	return 0;
}
