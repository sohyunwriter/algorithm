/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1026
*/

import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] a = new int[n];
		Integer[] b = new Integer[n];
		
		for(int i = 0; i < n; i++){
			a[i] = sc.nextInt();
		}
		
		for(int i = 0; i < n; i++){
			b[i] = sc.nextInt();
		}
		
		Arrays.sort(a);
		
		Arrays.sort(b, new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2){
				return o2 - o1;
			}
		});
		
		int ans = 0;
		
		for(int i = 0; i < n; i++){
			ans += a[i] * b[i];
		}
		
		System.out.println(ans);
	}

}
