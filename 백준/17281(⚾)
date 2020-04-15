#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 51
using namespace std;

int n, ans;
int board[MAX][MAX];

int cal(vector<int> v) {
	//for (auto i : v)
	//	cout << i << " ";
	//cout << endl;
	int score = 0;
	int outCount = 0;
	int nowpos = 0;
	for (int i = 0; i < n; i++) {
		vector<int> play;
		int base[3] = { 0, 0, 0 };
		while (outCount < 3) {
			int pos = v[nowpos];
			pos--;
			//cout << pos << " " << board[i][pos] << endl;
			if (board[i][pos] == 0) {
				outCount++;
			}
			else {
				for (int k = 2; k >= 0; k--) {
					if (base[k] == 1) {
						if (k + board[i][pos] >= 3) { //들어옴
							score++;
							base[k] = 0;
						}
						else {
							base[k + board[i][pos]] = 1;
							base[k] = 0;
						}
					}
				}//for
				if (board[i][pos] == 4) {
					score++;
				}
				else {
					base[board[i][pos]-1] = 1;
				}
			
			}//else 
			nowpos++;
			nowpos = nowpos % 9;

			//for (auto pair : play)
			//	cout << pair << " ";
			//cout << endl;
		}//while

		outCount = 0;
		for (int i = 0; i < play.size(); i++) {
			if (play[i] >= 4) {
				score++;
			}
		}		

	}

	if (score > ans) {
		ans = score;
	}

	return 0;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &board[i][j]);
		}
	}
	vector<int> a;

	for (int i = 2; i < 10; i++) {
		a.push_back(i);
	}

	do {
		vector<int> v; //(9) 하면 0 들어간다 주의**
		for (int i = 0; i < 3; i++) {
			v.push_back(a[i]);
		}
		v.push_back(1);
		for (int i = 3; i < 8; i++) {
			v.push_back(a[i]);
		}
		cal(v);

	} while (next_permutation(a.begin(), a.end()));

	cout << ans << endl;
	return 0;
}
