/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1107
*/

import java.util.*;

public class Main{
	
	public static int broken[] = new int[10];
	public static int possible(int c) {
		if( c == 0) {
			if(broken[0] == 1)
				return 0;
			else
				return 1;
		}
		
		int len = 0;
		while (c > 0) {
			if(broken[c%10] == 1) 
				return 0;
			
			len += 1;
			c /= 10;
		}
		
		return len;
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int m = sc.nextInt();
		for (int i = 0; i < m; i++) {
			int x = sc.nextInt();
			broken[x] = 1;
		}
		
		int ans = Math.abs(n - 100);
		
		for(int i = 0; i < 1000000; i++) {
			int c = i;
			int len = possible(c);
			int press = Math.abs(n - c);
			//2450=c 5457=n
			
			if(ans > len + press && len != 0)
				ans = len+press;
			
		}
		
		System.out.println(ans);
	}
	
}
