/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1920
*/

#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int n, m, num;
	scanf("%d", &n);

	set <int> a;
	for (int i = 0; i < n; i++) {
		scanf("%d", &num);
		a.insert(num);
	}

	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		scanf("%d", &num);
		if (a.find(num) == a.end())
			printf("0\n");
		else
			printf("1\n");
	}

	return 0;

}
