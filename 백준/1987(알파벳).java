/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1987
*/

import java.util.*;

public class Main {
	
	static char[][] a;
	static boolean[] visited;
	static boolean[][] isVisited;
	static int ans = 1;
	static int dx[] = {0, 0, 1, -1};
	static int dy[] = {1, -1, 0, 0};
	static int C, R;
	
	static void backFun(int i, int j, int sum){
		ans = Math.max(ans, sum);
	
		for(int l = 0; l < 4; l++){
			if(i+dx[l] >= 0 && i+dx[l] < C && j+ dy[l]>= 0 && j+dy[l] < R){
				int x = i + dx[l];
				int y = j+ dy[l];
				char alpha = a[x][y];
		
				if(visited[alpha - 'A'] == false && isVisited[x][y] == false){
					visited[alpha-'A'] = true;
					isVisited[x][y] = true;
					
					backFun(x, y, sum+1);
					
					isVisited[x][y] = false;
					visited[alpha-'A'] = false;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		
		a = new char[C][R];
		visited = new boolean['Z'-'A' + 1];
		isVisited = new boolean[C][R];
		sc.nextLine();
		
		for(int i = 0; i < R; i++){
			String s = sc.nextLine();
			
			for(int j = 0; j < C; j++){
				a[j][i] = s.charAt(j);
			}
		}
		
		visited[a[0][0] - 'A'] = true;
		isVisited[0][0] = true;
		backFun(0, 0, 1);
		System.out.println(ans);
	}
}
