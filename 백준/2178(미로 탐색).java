/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/2178
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
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		String s[] = new String[n];
		sc.nextLine();
		
		for(int i = 0; i < n; i++){
			s[i] = sc.nextLine();
		}
		
		boolean isVisited[][] = new boolean[n][m]; //정점 방문 여부 체크
		int dist[][] = new int[n][m];
				
		int dx[] = {0, 0, 1, -1};
		int dy[] = {1, -1, 0, 0};
		
		Queue<Pair> q = new LinkedList<Pair>();
		
		q.add(new Pair(0,0));
		dist[0][0] = 1;
		isVisited[0][0] = true;
		
		while(!q.isEmpty()){
			int x = q.peek().x;
			int y = q.peek().y;
			q.poll();
			
			if(x == n-1 && y == m-1)
				break;
			
			for(int i = 0; i < 4; i++){
				int nx = x + dx[i];
				int ny = y + dy[i];
				if(nx >= 0 && nx < n && ny >= 0 && ny < m){
					if(isVisited[nx][ny] == false && s[nx].charAt(ny) == '1'){
						dist[nx][ny] = dist[x][y] + 1;
						isVisited[nx][ny] = true;
						q.add(new Pair(nx, ny));
					}
					
				}
			}
		}//while
		
		System.out.println(dist[n-1][m-1]);
	}

}

