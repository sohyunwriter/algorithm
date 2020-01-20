import java.util.*;

public class Main {
	
	static char[] a;
	static boolean[] visited;
	static int m;
	
	static void backT(int depth, String password, char lastChar, int ja, int mo){
		//종료조건
		if(depth == m){
			if(ja >= 2 && mo >= 1){
				System.out.println(password);
				return;
			}
			else
				return;
		}
		
	
		for(int i = 0; i < a.length; i++){
			if(a[i] > lastChar && visited[i] == false){
				visited[i] = true;
				if(a[i] == 'a' || a[i] == 'e' || a[i] == 'i' || a[i] == 'o' || a[i] == 'u')
					backT(depth + 1, password + a[i], a[i], ja, mo+1);
				else
					backT(depth + 1, password + a[i], a[i], ja+1, mo);
				visited[i] = false;	
			}
		}
}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		m = sc.nextInt(); //만들어야하는 암호 문자열 수
		int n = sc.nextInt();
		
		a = new char[n];
		visited = new boolean[n];
		
		sc.nextLine();
		
		for(int i = 0; i < n; i++){
			String s = sc.next();
			a[i] = s.charAt(0);
			
		}
		
		Arrays.sort(a);
		
		backT(0, "", ' ', 0, 0);
			
	}
}
