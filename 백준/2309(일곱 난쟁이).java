/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2309
*/

import java.util.*;

public class Main {
	static int[] a;
	static boolean[] visited;
	static int print = 0;
	
	static void bt(int depth, int sum){
		if(depth == 7 && print == 0){
			if(sum == 100){
				for(int i = 0; i < 9; i++){
					if(visited[i] == true){
						System.out.println(a[i]);
					}
				}
				print = 1;
			}
			return;
		}
		
		for(int i = 0; i < 9; i++){
			if(visited[i] == false){
				visited[i] = true;
				bt(depth+1, sum+a[i]);
				visited[i] = false;
			}
		}
		
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		//BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		a = new int[9];
		visited = new boolean[9];
		
		for(int i = 0; i < 9; i++){
			a[i] = sc.nextInt();
		}
		
		Arrays.sort(a);
		bt(0, 0);
		
	}
}
