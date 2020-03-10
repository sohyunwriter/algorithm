#include <iostream>
#include <vector>
using namespace std;

//0번부터 차례대로 번호 매겨진 n개의 원소 중 네 개를 고르는 모든 경우 출력
void forPick(int n) {
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for(int k = j + 1; k < n; k++) {
				for (int l = k + 1; l < n; l++) {
					cout << i << " 대" << j << " " << k << " " << l << endl;
				}//for
			}//for
		}//for
	}//for
}

//n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
void recursivePick(int n, vector<int>& picked, int toPick) { 
	// n : 원소들의 총 개수, picked : 지금까지 고른 원소들의 번호, toPick: 더 고를 원소들의 개수
 	// 일 때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력
  
	if (toPick == 0) { //base case : 더 고를 원소가 없을 때 고른 원소들을 출력
		for (int i = 0; i < picked.size(); i++) {
			cout << picked[i] << " ";
		}
		cout << endl;

		return;
	}

	//고를 수 있는 가장 작은 번호 계산
	int smallest = picked.empty() ? 0 : picked.back() + 1;
  	//이 단계에서 원소를 하나 고름
	for (int next = smallest; next < n; next++) {
		picked.push_back(next);
		recursivePick(n, picked, toPick-1);
		picked.pop_back();
	}
}

int main() {
	int N = 6;
	vector<int> a;

	printf("---forPick print---\n");
	forPick(N);

	printf("---recursivePick print---\n");
	recursivePick(N, a, 4);

	return 0;
}
