#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mylowerbound(vector<int> v, int target) { //lowerbound
	sort(v.begin(), v.end());
	
	int start = 0;
	int end = v.size();
	int mid;

	while (start < end) { //start == end가 되는 시점 종료
		mid = (start + end) / 2;

		if (v[mid] >= target)
			end = mid;
		else
			start = mid + 1;

	}
	return end; // 또는 start 반환해도 됨
}

int main() { /* this is for test */
	vector<int> v;
	int n, target, input;
	scanf("%d %d", &n, &target);
	for (int i = 0; i < n; i++) {
		scanf("%d", &input);
		v.push_back(input);
	}
	sort(v.begin(), v.end());

	int ans1 = mylowerbound(v, target);
	vector<int>::iterator iter;
	iter = lower_bound(v.begin(), v.end(), target);
	int reans1 = iter - v.begin();

	cout << ans1 << " " << reans1 << endl;

	return 0;
}
