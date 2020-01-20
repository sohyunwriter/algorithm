/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2096
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int minSum, maxSum;
	int a[3];
	int mina[2][3] = { 0, };
	int maxa[2][3] = { 0, };;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%d", &a[j]);
		}		
		mina[1][0] = min(a[0] + mina[0][0], a[0] + mina[0][1]);
		maxa[1][0] = max(a[0] + maxa[0][0], a[0] + maxa[0][1]);
		mina[1][1] = min(min(mina[0][0]+a[1], mina[0][1] + a[1]), a[1]+mina[0][2]);
		maxa[1][1] = max(max(maxa[0][0] + a[1], maxa[0][1] + a[1]), a[1]+maxa[0][2]);
		mina[1][2] = min(a[2] + mina[0][1], a[2] + mina[0][2]);
		maxa[1][2] = max(a[2] + maxa[0][1], a[2] + maxa[0][2]);
		
		for (int j = 0; j < 3; j++) {
			mina[0][j] = mina[1][j];
			maxa[0][j] = maxa[1][j];
		}

		//printf("min %d %d %d \n", mina[1][0], mina[1][1], mina[1][2]);
		//printf("max %d %d %d \n", maxa[1][0], maxa[1][1], maxa[1][2]);

	}
	minSum = min(min(mina[1][0], mina[1][1]), mina[1][2]);
	maxSum = max(max(maxa[1][0], maxa[1][1]), maxa[1][2]);
	
	printf("%d %d", maxSum, minSum);

	return 0;



}
