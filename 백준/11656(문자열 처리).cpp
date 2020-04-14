#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string s;
	vector<string> v;

	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		v.push_back(s.substr(i));
	}

	sort(v.begin(), v.end());

	for (auto i : v)
		cout << i << endl;

	return 0;
}
