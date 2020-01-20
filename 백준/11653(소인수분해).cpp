/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11653
*/

#include <iostream>
using namespace std;

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 2; i * i <= n; i++) {
		while (n % i == 0) {
			cout << i << endl;
			n /= i;
		}
	}

	if (n > 1)
		cout << n << endl;

	return 0;
}
