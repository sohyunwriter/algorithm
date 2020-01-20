/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2003
*/

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int a[] = new int[N+1];
		
		for (int i = 0; i < N; i++) {
			a[i] = sc.nextInt();
			
		}
		int ans = 0;
		
		for (int i = 0; i < N; i++) {
			int k = 0;
			k += a[i];
			if (k == M) {
				ans+=1;
				continue;
			}
			if(k < M) {
				for (int j = i+1; j < N; j++) {
					k += a[j];
					if(k == M){
						ans += 1;
						break;
					}
					if(k > M) {
						break;
					}
				}
			}
		}	
		
		System.out.println(ans);
		
	}
	
}
