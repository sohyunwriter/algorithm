/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11048
*/

import java.util.*;

public class Main {
	
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[][] a = new int[n+1][m+1];
		
		for (int i = 1; i <= n; i++) {
			for(int j = 1; j<= m; j++) {
				a[i][j] = sc.nextInt();
			}
		}
		
		int[][] d = new int[n+1][m+1];
		
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j<= m; j++) {
				d[i][j] = d[i-1][j] + a[i][j];
				d[i][j] = Math.max(d[i][j], d[i][j-1] + a[i][j]);
				d[i][j] = Math.max(d[i][j], d[i-1][j-1] + a[i][j]);
			}
		}
		
		System.out.println(d[n][m]);
		
	}

}
