#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int T, n, m;
	int a[30][30] = { 0 };

	for (int i = 1; i <= 29; i++) {
		for (int j = 0; j <= 29; j++) {
			if (i == j || j == 0) {
				a[i][j] = 1;
				continue;
			}
			a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
		}
	}

	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d %d", &n, &m);
		printf("%d\n", a[m][n]);
	}
	return 0;
}
