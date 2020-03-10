#include <iostream>
using namespace std;

//필수 조건 : n >= 1
//1부터 n까지 합을 계산하는 반복 함수
//3가지 방법 - 1) for 2) recursion 3) tail recursion
int sum(int n) { //for
	int ret = 0;
	for (int i = 1; i <= n; i++)
		ret += i;

	return ret;
}

int recursiveSum(int n) { //recursion
	if (n == 1)
		return 1;

	return n + recursiveSum(n - 1); //아직 계산해야할 게 남아 있으므로 스택에 쌓임
}

int tailRecursiveSum(int n, int sum) { //tail recursion
	if (n == 1)
		return (sum+1);

	return tailRecursiveSum(n - 1, sum + n); //recursiveSum과 달리 스택에 쌓이지 않음
}

int main() {
	int N = 10;

	int ans1 = sum(N); //55
	int ans2 = recursiveSum(N); //55
	int ans3 = tailRecursiveSum(N, 0); //55

	cout << "ans1: " << ans1 << endl;
	cout << "ans2: " << ans2 << endl;
	cout << "ans3: " << ans3 << endl;

	return 0;
}
