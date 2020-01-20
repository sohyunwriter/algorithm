/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11051
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, k;
	scanf("%d %d", &n, &k);
	long long d[1001][1001];

	d[0][0] = 1;
	
	for (int i = 1; i <= 1000; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i) 
				d[i][j] = 1;
			else
				d[i][j] = ((d[i - 1][j - 1] % 10007) + (d[i - 1][j] % 10007)) % 10007;
		}
	}

	cout << d[n][k];
	return 0;
}
