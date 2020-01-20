/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/10819
*/

import java.util.*;

public class Main {
	
	static int[] a;
	static boolean[] visited;
	static int max = 0;
	
	static void backFun(int depth, int sum, int last){
		
		if(depth == a.length){
			max = Math.max(max, sum);
			return;
		}
		
		for(int i = 0; i < a.length; i++){
			
			if(visited[i] == false){
				visited[i] = true;
				if(depth == 0)
					sum = 0;
				else
					sum+= Math.abs(last- a[i]);
				
				backFun(depth+1, sum, a[i]);
				
				if(depth != 0)
					sum-= Math.abs(last-a[i]);
				visited[i] = false;
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		a = new int[n];
		visited = new boolean[n];
		
		for(int i = 0; i < n; i++){
			a[i] = sc.nextInt();
		}
		
		backFun(0, 0, 0);
		System.out.println(max);
	}
}
