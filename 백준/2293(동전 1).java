/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2293
*/

import java.util.*;

public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] a = new int[n+1];
		for(int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}
		
		int[][] d = new int[n+1][m+1];
		
		d[0][0] = 1;
		for(int i = 1; i <= n; i++) {
			for(int j = 0; j<= m; j++) {
				d[i][j] = d[i-1][j]; //i번째를 사용하지 않는 경우
				if(j - a[i] >= 0) {
					d[i][j] += d[i][j-a[i]]; //i번째를 사용하는 경우 
				}
			}
		}
		
		System.out.println(d[n][m]);
		
	}
}
