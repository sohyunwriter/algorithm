/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1012
*/

import java.util.*;

public class Main {
	
	static int[][] map;
	static boolean isVisited[][];
	static int x[] = {-1, 1, 0, 0};
	static int y[] = {0, 0, -1, 1};
	static int m, n;
	
	static void dfs(int i, int j){
		isVisited[i][j] = true;
		
		for(int l = 0; l < 4; l++){
			if(i+x[l] < m && i+x[l] >= 0 && j+y[l] < n && j+y[l] >= 0){
				if(isVisited[i+x[l]][j+y[l]] == false && map[i+x[l]][j+y[l]] == 1){
					//System.out.println("중간: "+ i+x[l]+", "+ j+y[l]);
					dfs(i+x[l], j+y[l]);
				}	
			}
		}
		
	}
	
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		int tn = sc.nextInt();
		
		StringBuilder sb = new StringBuilder();
		int ans = 0;
		
		while(tn > 0){
			m = sc.nextInt();
			n = sc.nextInt();
			int k = sc.nextInt();
			
			map = new int[m][n];
			isVisited = new boolean[m][n];
			
			for(int i = 0; i < k; i++){
				int a = sc.nextInt();
				int b = sc.nextInt();
				map[a][b] = 1;
				//System.out.println(a + ":" + b);
			}
			
			for(int i = 0; i < m; i++){
				for(int j = 0; j < n; j++){
					//배추가 있고, 방문하지 않았을 때
					if(map[i][j] == 1 && isVisited[i][j] == false){
						dfs(i, j);
						ans++;
					}
				}
			}//for
			
			sb.append(ans);
			sb.append('\n');
			ans = 0;
			tn--;
		}
		
		System.out.println(sb);
		
	}
}
