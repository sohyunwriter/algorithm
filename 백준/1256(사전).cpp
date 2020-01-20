/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1256
*/

#include <iostream>
#include <algorithm>
#include <string>
#define ll double
using namespace std;



int main() {
	int n, m, k;
	scanf("%d %d %d", &n, &m, &k);
	ll d[201][201];

	d[0][0] = 1;
	for (int i = 1; i <= n + m; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i)
				d[i][j] = 1;
			else
				d[i][j] = d[i - 1][j - 1] + d[i - 1][j];
		}
	}

	/*
	for (int i = 1; i <= n+m; i++) {
		for (int j = 0; j <= i; j++)
			cout << d[i][j] << " ";
		printf("\n");
	}
	*/

	if (d[n + m][n] < k) {
		printf("-1");
		return 0;
	}

	string ans;

	while (n != 0 || m != 0) {
		//cout << d[n + m - 1][n - 1] << endl;
		if (d[n + m - 1][n - 1] < k) { // z
			k -= d[n + m - 1][n - 1];
			ans.push_back('z');
			m--;
			//cout << ans << endl;
		}
		else {
			ans.push_back('a');
			//cout << ans << endl;
			n--;
		}
	}

	while (n--)
		ans.push_back('a');

	while (m--)
		ans.push_back('z');

	cout << ans;
	return 0;
}
