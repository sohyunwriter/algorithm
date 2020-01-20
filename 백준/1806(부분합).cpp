#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, s;
	scanf("%d %d", &n, &s);
	int a[100000];
	int ans = 987654321;
	long long sum = 0;

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	
	int tail = 0;
	int cnt = 0;
	for (int head = 0; head <= n; head++) {
		sum += a[head];
		cnt++;
		while (sum >= s) {
			ans = min(ans, cnt);
			sum -= a[tail++];
			cnt--;
		}

	}
	if (ans == 987654321)
		cout << '0';
	else
		cout << ans;

	return 0;
}
