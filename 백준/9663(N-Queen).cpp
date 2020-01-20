/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/9663
*/

#include <iostream>
using namespace std;

int col[15];
int n;
int ans = 0;

int check(int i) {
	for (int j = 0; j < i; j++) {
		if (col[j] == col[i] || abs(col[i] - col[j]) == (i - j))
			return 0;
	}
	return 1;
}

void nqueen(int row) {
	if (row == n) 
		ans++;
	
	else {
		for (int i = 0; i < n; i++) {
			col[row] = i;
			if (check(row))
				nqueen(row + 1);
		}

	}


}

int main() {
	scanf("%d", &n);
	nqueen(0);
	cout << ans;
	return 0;

}
