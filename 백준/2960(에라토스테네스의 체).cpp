/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2960
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int	arr[1001] = { 0, };
	int n, k;
	scanf("%d %d", &n, &k);
	int cnt = 0;
	int ans = 0;

	for (int i = 2; i <= n; i++) {
		if (arr[i] == 0) {
			for (int j = i; j <= n; j++) {
				if (j % i == 0) {
					if (arr[j] == 0) {
						cnt++;
						if (cnt == k)
							ans = j;
					}
					arr[j]++;
				}
			}
		}
	}
	cout << ans;
	return 0;
}
