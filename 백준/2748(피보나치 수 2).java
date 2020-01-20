/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2748
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] a = new long[N+1];
		a[0] = 0;
		a[1] = 1;
		
		for(int i = 2; i < a.length; i++) {
			a[i] = a[i-1] + a[i-2];
		}
		System.out.println(a[N]);
		
	}

}
