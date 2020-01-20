/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2583
*/

import java.util.*;

public class Main {
	
	static int[][] map;
	static boolean isVisited[][];
	static int x[] = {-1, 1, 0, 0};
	static int y[] = {0, 0, -1, 1};
	static int m, n;
	static int size = 0;
	static int cnt = 0;
	
	static void dfs(int i, int j){
		size+=1;
		isVisited[i][j] = true;
		
		for(int l = 0; l < 4; l++){
			if(i+x[l] < n && i+x[l] >= 0 && j+y[l] < m && j+y[l] >= 0){
				if(isVisited[i+x[l]][j+y[l]] == false && map[i+x[l]][j+y[l]] == 0){
					dfs(i+x[l], j+y[l]);
				}	
			}
		}
		
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		m = sc.nextInt();
		n = sc.nextInt();
		int k = sc.nextInt();
		
		int ans = 0;
		
		map = new int[n][m];
		
		isVisited = new boolean[n][m];
			
		for(int i = 0; i < k; i++){
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			for(int j = x1; j < x2; j++){
				for(int l = y1; l < y2; l++){
					map[j][l] = 1;
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		
		int[] sizeAll = new int[m*n];
		
		//dfs
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(map[i][j] == 0 && isVisited[i][j] == false){
					dfs(i, j);
					cnt++;
					//System.out.println(size);
					sizeAll[cnt] = size;
					size = 0;
				}
			
			}
		}
		
		System.out.println(cnt);
		
		for(int i = 1; i <= cnt; i++){
			for(int j = i; j <= cnt; j++){
				if(sizeAll[i] > sizeAll[j]){
					int temp = sizeAll[i];
					sizeAll[i] = sizeAll[j];
					sizeAll[j] = temp;
				}
			}
		}
		
		for(int i = 1; i<= cnt; i++){
			System.out.print(sizeAll[i] + " ");
		}
		
	}
}
