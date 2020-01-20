/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/7578
*/

import java.util.*;

class Pair{
	int x;
	int y;
	
	Pair(int x, int y){
		this.x = x;
		this.y = y;
	}
}

public class Main {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt();
		int n = sc.nextInt();
		
		int[][] a = new int[n][m];
		Queue<Pair> q = new LinkedList<Pair>();
		int dist[][] = new int[n][m]; //일수
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				a[i][j] = sc.nextInt();
				if(a[i][j] == 1){
					q.add(new Pair(i, j));	
					dist[i][j] = 0;
				}
				else if(a[i][j] == 0){
					dist[i][j] = -1;
				}
				else
					dist[i][j] = 0;
			}
		}
		
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		
		while(!q.isEmpty()){
			int x = q.peek().x;
			int y = q.peek().y;
			q.poll();
			
			for(int i = 0; i < 4; i++){
				if(x+dx[i] >= 0 && x+dx[i] < n && y+dy[i] >= 0 && y+dy[i] < m){
					int nx = x+dx[i];
					int ny = y+dy[i];
					//토마토가 있는데 아직 방문하지 않은 곳
					if(dist[nx][ny] == -1 && a[nx][ny] == 0){
						dist[nx][ny] = dist[x][y] + 1;	
						//System.out.println("ww " +nx+ ", " +ny);
						q.add(new Pair(nx, ny));
					}
				}
			}//for
			
		}
		
		int ans = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(dist[i][j] > 0){
					ans = Math.max(ans, dist[i][j]);	
				}
			}
		}//for
	
		//안익은 토마토
		int remain = 0;
		//다 익은 토마토
		int zeroCount = 0;
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(a[i][j] != 0){
					zeroCount++;
				}
				if(dist[i][j] == -1){
					remain++;
				}
			}
		}//for
		
		if(remain == 0 && zeroCount != m*n)
			System.out.println(ans);
		else if(remain != 0)
			System.out.println(-1);
		else
			System.out.println(0);
	}

}

