/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1927
*/

import java.util.*;

public class Main{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		PriorityQueue<Integer> q = new PriorityQueue<Integer>();
		int n = sc.nextInt();
		
		while(n-- > 0) {
			int x = sc.nextInt();
			if(x == 0) {
				if(q.isEmpty()) {
					System.out.println(0);
				} else {
					System.out.println(q.poll());
				}
			}else {
				q.offer(x);
			}
		}
		
	}
}
