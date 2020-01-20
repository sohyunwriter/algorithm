/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11399
*/

import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[] a = new int[n+1];
		
		for(int i = 1; i <= n; i++){
			a[i] = sc.nextInt();
		}
		
		Arrays.sort(a, 1, n+1);
		
		int sum[] = new int[n+1];
		
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= i; j++){
				sum[i] += a[j];
			}
		}
		
		int ans = 0;
		
		for(int i = 1; i <= n; i++){
			ans += sum[i];
		}
	
		System.out.println(ans);
	}

}
