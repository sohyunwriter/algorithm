import java.util.*;

public class Main {
	
	static List<Integer> list[];
	static boolean isVisited[];
	static boolean isVisited2[];
	
	static void dfs(int node){
		System.out.print(node + " ");
		
		isVisited[node] = true;
		
		for(int i = 0; i < list[node].size(); i++){
			int x = list[node].get(i);
			if(isVisited[x] == false){
				dfs(x);
			}
		}
	}
	
	static void bfs(int node){
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(node);
		isVisited2[node] = true;
		System.out.print(node);
		
		while(!q.isEmpty()){
			int x = q.poll();
			if(x != node)
				System.out.print(" " + x);
		
			for(int i = 0; i < list[x].size(); i++){
				int y = list[x].get(i);
				if(isVisited2[y] == false){
					isVisited2[y] = true;
					q.add(y);
				}
			}
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int start = sc.nextInt(); //탐색 시작 정점
		
		list = (ArrayList<Integer>[]) new ArrayList[n+1];
		for(int i = 1; i<= n; i++){
			list[i] = new ArrayList<Integer>();
		}
		
		for(int i = 0; i < m; i++){
			int a = sc.nextInt();
			int b = sc.nextInt();
			list[a].add(b);
			list[b].add(a);
		}
		
		for(int i = 1; i <= n; i++){
			Collections.sort(list[i]);
		}
		
		isVisited = new boolean[n+1];
		isVisited2 = new boolean[n+1];
		
		dfs(start);
		System.out.println();
		bfs(start);
	}

}
