/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2606
*/

import java.util.*;

public class Main {
	static boolean isVisited[];
	static int n;
	static int[][] map;
	static int ans;
	
	static int dfs(int node){
		isVisited[node] = true;
		for(int i = 2; i<= n; i++){
			if(isVisited[i] == false && map[node][i] != 0){
				//System.out.println("다음 " +i);
				ans++;
				//System.out.println("ans " +ans);
				dfs(i);
			}
		}
		return 0;
	}
	
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		int m = sc.nextInt();
		
		isVisited = new boolean[n+1];
		
		map = new int[n+1][n+1];
		
		for(int i = 0; i< m; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			map[a][b] = 1;
			map[b][a] = 1;
		}
		
		ans = 0;
		
		isVisited[1] = true;
		
		for(int i = 1; i<= n; i++){
			if(map[i][1] != 0 && isVisited[i] == false){
				//System.out.println("시작 " +i);
				ans++;
				dfs(i);
			}	
		}
		
		System.out.println(ans);
		
	}
}
