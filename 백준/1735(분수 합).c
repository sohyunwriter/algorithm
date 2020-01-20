#include <stdio.h>

long gcd(long a, long b) {
	if (b == 0)
		return a;
	else
		gcd(b, a%b);
}

int main() {
	long a, b, c, d;
	long bottom, top;
	long gcdNum;

	scanf("%ld %ld", &a, &b);
	scanf("%ld %ld", &c, &d);

	bottom = b * d;
	top = a * d + b * c;
	gcdNum = gcd(top, bottom);
	bottom /= gcdNum;
	top /= gcdNum;

	printf("%ld %ld\n", top, bottom);

	return 0;
}
