/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11724
*/

import java.util.*;
public class Main {
	static boolean isVisited[];
	static int[][] map;
	static int node;
	static int count = 0;
	
	public static void dfs(int n){
		//System.out.println(n);
		isVisited[n] = true;
		for(int i = 1; i <= node; i++){
			if(isVisited[i] == false && map[n][i] != 0){
				dfs(i);
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		node = sc.nextInt();
		int m = sc.nextInt();
		
		
		map = new int[node+1][node+1];
		isVisited = new boolean[node+1];
		for(int i = 0; i < m; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			map[a][b] = 1;
			map[b][a] = 1;
		}
		
		for(int i = 1; i<= node; i++){
			if(isVisited[i] == false){
				dfs(i);
				count++;
			}
		}
		
		System.out.println(count);
	}

}
