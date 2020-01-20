/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2748
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	long long n;
	cin >> n;
	long long prev = 0;
	long long cur = 1;
	long long ans;

	if (n == 0)
		ans = 0;
	else if (n == 1)
		ans = 1;
	else {
		while (--n) {
			ans = prev + cur;
			prev = cur;
			cur = ans;
		}
	}
	cout << ans;

	return 0;



}
