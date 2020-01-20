/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2003
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	long long m;
	scanf("%d %lld", &n, &m);
	int a[10000];
	int ans = 0;
	long long sum = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	
	int tail = 0;
	for (int head = 0; head <= n; head++) {
		sum += a[head];
		while (sum >= m) {
			if (sum == m)
				ans++;
			sum -= a[tail++];
		}

	}

	cout << ans;

	return 0;
}
