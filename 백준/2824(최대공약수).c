/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2824
*/

#include <stdio.h>

long long gcd(long long a, long long b) {
	if (b == 0)
		return a;
	return gcd(b, a%b);
}

int main() {
	long long n, m;
	long long a[1001];
	long long b[1001];

	scanf("%lld", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lld", &a[i]);
	}

	scanf("%lld", &m);
	for (int i = 0; i < m; i++) {
		scanf("%lld", &b[i]);
	}

	long long gcdNum = 1;
	long long pgcdNum = 1;
	int flag = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			pgcdNum= gcd(a[i], b[j]);
			gcdNum *= pgcdNum;
			if (gcdNum >= 1000000000) {
				gcdNum %= 1000000000;
				flag = 1;
			}
			b[j] /= pgcdNum;
			a[i] /= pgcdNum;
		}
	}

	if (flag) {
		int cnt = 0;
		gcdNum %= 1000000000;
		long long copy = gcdNum;
		while (copy / 10 != 0) {
			copy /= 10;
			cnt++;
		}
		for (int i = 1; i < 9 - cnt; i++)
			printf("0");
		printf("%lld", gcdNum);
		
	}
	else
		printf("%lld\n", gcdNum);

	return 0;
}
