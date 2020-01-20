/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2156
*/

import java.util.*;

public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n+1];
		for(int i = 1; i<=n; i++) {
			a[i] = sc.nextInt();
		}
		
		int[] d = new int[n+1];

		d[1] = a[1];
		if(n >= 2) {
			d[2] = a[1] + a[2];
		}
		
		for(int i = 3; i<=n; i++) {
			d[i] = d[i-1]; //i번째 잔을 마시지 않을 경우(0번 연속)
			d[i] = Math.max(d[i], d[i-2]+a[i]); //i-1번재 잔을 마시지 않은 경우(1번 연속) 
			d[i] = Math.max(d[i], d[i-3]+a[i-1]+a[i]); //i-1번째 잔, i번째 잔 마셔서 2번 연속 + 3번 연속 방지(i-2는 마시지 않기) (2번 연속)
		}
		
		int ans = d[1];
		
//		for(int i =2; i<=n; i++) {
//			ans = Math.max(ans, d[i]);
//		}
		
		System.out.println(d[n]);
	}
}
