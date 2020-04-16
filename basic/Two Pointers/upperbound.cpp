#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int myupperbound(vector<int> v, int target) { //upperbound
	int start = 0;
	int end = v.size();
	int mid;

	while (start < end) { // start == end가 되는 시점 종료
		mid = (start + end) / 2;

		if (v[mid] > target)
			end = mid;
		else
			start = mid + 1;
	}
	return end;
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
  
	int ans2 = myupperbound(v, target);
	iter = upper_bound(v.begin(), v.end(), target);
	int reans2 = iter - v.begin();
	cout << ans2 << " " << reans2 << endl;

	return 0;
}
