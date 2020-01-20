/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2096
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		int N = sc.nextInt();
		int[] a = new int[N*3];
		for(int i = 0; i < N*3; i++) {
			a[i] = sc.nextInt();
		}
		
		long[] min = new long[3];
		long[] max = new long[3];
		
		min[0] = a[0]; min[1] = a[1]; min[2] = a[2];
		max[0] = a[0]; max[1] = a[1]; max[2] = a[2];
		
		for(int i = 1; i < N; i++) {
			//System.out.println(min[2] + " " + max[2]);
			long temp1 = min[0]; long temp2 = min[1]; long temp3 = min[2];
			long temp4 = max[0]; long temp5 = max[1]; long temp6 = max[2]; 
			
			min[0] = a[i*3] + Math.min(min[0], min[1]);
			max[0] = a[i*3] + Math.max(max[0], max[1]);
			
			min[2] = a[i*3 + 2] + Math.min(temp2, temp3);
			max[2] = a[i*3 + 2] + Math.max(temp5, temp6);
			
			
			long mint = Math.min(temp1, temp2);
			mint = Math.min(mint, temp3);
			long maxt = Math.max(temp4, temp5);
			maxt = Math.max(maxt, temp6);
			
			min[1] = a[i*3 + 1] + mint;
			max[1] = a[i*3 + 1] + maxt;
			
		}
		
		
		System.out.println(Math.max(max[2], Math.max(max[0], max[1])) + " " + Math.min(min[2], Math.min(min[0], min[1])) );
		
	}

}
