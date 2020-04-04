//문제 - https://www.acmicpc.net/problem/1986
//내 코드 설명 - https://sohyunwriter.tistory.com/69

#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <algorithm>
#define MAX 1001
using namespace std;

char board[MAX][MAX];
bool check[MAX][MAX];
int n, m;
int kx[8] = { -2, -2, 2, 2, -1, -1, 1, 1 };
int ky[8] = { -1, 1, -1, 1, -2, 2, -2, 2 };
int c[8] = { 0, 0, -1, 1, -1, 1, -1, 1 };
int d[8] = { -1, 1, 0, 0, -1, 1, 1, -1 };

int main() {
	int k, q, p;
	int row, col;
	int ans = 0;

	scanf("%d %d", &n, &m);
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= m; j++) {
			board[i][j] = NULL;
		}
	}
	
	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		scanf("%d %d", &row, &col);
		board[row][col] = 'Q'; // knight
		check[row][col] = true;
	}

	scanf("%d", &q);
	for (int i = 0; i < q; i++) {
		scanf("%d %d", &row, &col);
		board[row][col] = 'K'; // queen
		check[row][col] = true;
	}

	scanf("%d", &p);
	for (int i = 0; i < p; i++) {
		scanf("%d %d", &row, &col);
		board[row][col] = 'P'; // pawn
		check[row][col] = true;
	}

	//search
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (board[i][j] == 'Q') {
				for (int l = 0; l < 8; l++) {
					int nrow = i + c[l];
					int ncol = j + d[l];
					while (1) {
						if (nrow < 1 || ncol < 1 || nrow > n || ncol > m)
							break;
						if (board[nrow][ncol] != NULL)
							break;

						check[nrow][ncol] = true;
						nrow = nrow + c[l];
						ncol = ncol + d[l];
					}
				}
			}
			else if (board[i][j] == 'K') {
				for (int l = 0; l < 8; l++) {
					int nrow = i + kx[l];
					int ncol = j + ky[l];
					if (0 < nrow && nrow <= n && 0 < ncol && ncol <= m) {
						check[nrow][ncol] = true;
					}
				}
			}
		}
	}

	/*
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (check[i][j] == true)
				cout << 1 << " ";
			else cout << 0 << " ";
		}
		cout << "\n";
	}
	*/

	//ans
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (check[i][j] == false && board[i][j] == NULL) {
				ans++;
			}
		}
	}

	cout << ans;

	return 0;
}
