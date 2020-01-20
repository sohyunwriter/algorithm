/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/11723
*/

import java.util.*;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = 20;
		int s = 0;
		int x;
		StringBuilder ans = new StringBuilder();
		
		while(m-- > 0) {
			String b = sc.next();
			if("add".equals(b)) {
				x = sc.nextInt();
				x--;
				s = s|(1<<x);
			} else if ("remove".equals(b)){
				x = sc.nextInt();
				x--;
				s = s & ~(1<<x);
			} else if("check".equals(b)) {
				x = sc.nextInt();
				x--;
				int res = s & (1<<x);
				if(res > 0) {
					ans.append("1\n");
					//System.out.println(1);
				} else if (res == 0) {
					ans.append("0\n");
					//System.out.println(0);
				}
			} else if("toggle".equals(b)) {
				x = sc.nextInt();
				x--;
				s = (s^(1<<x));
			} else if("all".equals(b)) {
				s = (1<<n) - 1;
			} else if("empty".equals(b)) {
				s = 0;
			}
			
		}
		
		System.out.println(ans);
		
	}
	
}
