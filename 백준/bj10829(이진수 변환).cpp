//https://sohyunwriter.tistory.com/95

#include <iostream>
#include <vector>
#include <algorithm> //reverse
using namespace std;

vector<int> toBinary(long long n) {
	vector<int> v;
	while (n != 0) {
		if (n % 2 == 0)
			v.push_back(0);
		else
			v.push_back(1);
		n /= 2;
	}
	reverse(v.begin(), v.end());
	return v;
}

int main() {
	long long N;
	scanf("%lld", &N);
	for (auto i : toBinary(N))
		cout << i;

	return 0;
}
