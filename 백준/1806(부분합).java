/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1806
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int ans = 0;
		
		int[] a = new int[N];
		for(int i = 0; i < N; i++) {
			a[i] = sc.nextInt();
		}
		
		for(int i = 0; i < N; i++) {
			long k = a[i];
			if(k == M) {
				ans = 1;
				break;
			}
			int temp = 0;
			if(k < M) {
				for(int j = i+1; j < N; j++) {
					k += a[j];
					if(k >= M) {
						temp += j - i + 1;
						if (ans == 0 || temp < ans) {
							ans = temp;
							break;
						}
						break;
					}
				}
			}
		}
		
		System.out.print(ans);
	}

}
