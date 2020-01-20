/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2294
*/

import java.util.*;

public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int[] a = new int[n+1];
		for(int i = 1; i <=n; i++) {
			a[i] = sc.nextInt();
		}
		
		int[] d = new int[m+1];
		
		d[0] = 0;
		
		//접근하지 않은 d[]
		for(int i = 1; i<= m; i++) {
			d[i] = -1;
		}
		
		for(int i = 1; i<=n; i++) {
			for(int j = 0; j<= m; j++) {
				if(j-a[i] >= 0 && d[j-a[i]] != -1) {
					if(d[j] == -1 || d[j] > d[j-a[i]] + 1) {
						d[j] = d[j-a[i]] + 1;
					}
				}
			}
		}
		
		System.out.println(d[m]);
		
	}
}
