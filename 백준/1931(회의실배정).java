/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1931
*/

import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[][] a = new int[n][2];
		
		for(int i = 0; i < n; i++){
			a[i][0] = sc.nextInt();
			a[i][1] = sc.nextInt();
		}
		
		Arrays.sort(a, new Comparator<int[]>() {
			@Override
			public int compare(final int[] o1, final int[] o2){
				final Integer x = o1[1];
				final Integer y = o2[1];
				
				if(x == y){
					final Integer a = o1[0];
					final Integer b = o2[0];
					return Integer.compare(a, b);
				}else{
					return Integer.compare(x, y);
				}
			}
		});
		
		int ans = 0;
		int endTime = -1;
		
		for(int i = 0; i < n; i++){
			if(a[i][0] >= endTime){
				ans+= 1;
				endTime = a[i][1];
			}
		}
		
		System.out.println(ans);
	}

}
