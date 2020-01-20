/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/6588
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int arr[1000001] = { 0, };
	int n = 0;

	for (int i = 2; i <= 1000000; i++) {
		if (arr[i] == 0) {
			for (int j = i + i; j <= 1000000; j += i) {
				arr[j]++;
			}
		}
	}

	while (true) {
		scanf("%d", &n);
		int flag = 0;
		if (n == 0)
			break;

		for (int i = 3; i <= n; i++) {
			if (arr[i] == 0) {
				if (arr[n - i] == 0) {
					printf("%d = %d + %d\n", n, i, n - i);
					flag = 1;
					break;
				}
			}
		}

		if (flag == 0)
			printf("Goldbach's conjecture is wrong.\n");

	}
	return 0;
}
