/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/10974
*/

import java.util.*;

public class Main{
	public static boolean next_permutation(int[] a) {
		int i = a.length - 1;
		while(i > 1 && a[i-1] > a[i]) {
			i -= 1;
		}
		
		if(i == 1)
			return false;
		
		int j = a.length - 1;
		while(a[i-1] > a[j] && j >= i) {
			j -= 1;
		}
		
		//바꾸기
		int temp = a[i-1];
		a[i-1] = a[j];
		a[j] = temp;
		
		j = a.length - 1;
		
		while ( i < j ) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i+= 1;
			j-= 1;
		}
		
		return true;
		
	}
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[] a = new int[n+1];
		for(int i = 1; i <= n; i++) {
			a[i] = i;
		}
		
		do {
			for(int i = 1; i <= n; i++) {
				System.out.print(a[i] + " ");
			}
			System.out.println();
		}while(next_permutation(a));
		
	}
}
