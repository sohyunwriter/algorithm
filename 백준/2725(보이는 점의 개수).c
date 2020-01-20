/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2725
*/

#include <stdio.h>

int gcd(int a, int b) {
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

int main() {
	int a[1001];

	for (int i = 1; i <= 1000; i++) {
		a[i] = i;
	}

	for (int i = 2; i <= 1000; i++) {
		for (int j = i; j <= 1000; j++) {
			if (gcd(j, i) != 1) {
				a[j]--;
			}
		}
	}

	int C, N;
	scanf("%d", &C);
	for (int i = 0; i < C; i++) {
		scanf("%d", &N);
		
		int cnt = 3;

		for (int j = 2; j <= N; j++) {
			cnt += (a[j] * 2);
		}
		
		printf("%d\n", cnt);
	}

	return 0;
}
