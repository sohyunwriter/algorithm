#include <cstdio>
#include <iostream>

using namespace std;

int main() {	
	int ax, ay, bx, by, cx, cy;
	long long result;

	scanf("%d %d %d %d %d %d", &ax, &ay, &bx, &by, &cx, &cy);

	result = (ax*by + bx*cy + cx*ay) - (ay*bx + by*cx + cy*ax);

	if (result > 0)
		cout << "1";
	else if (result < 0)
		cout << "-1";
	else
		cout << "0";

	return 0;

}
