#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, k;
	int ans = 1;
	scanf("%d %d", &n, &k);
	int j = k;

	while (j >= 1) {
		ans *= n;
		j--;
		n--;
	}

	while (k >= 1) {
		ans /= k;
		k--;
	}
	cout << ans;
	return 0;
}
