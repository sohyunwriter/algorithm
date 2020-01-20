/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1205
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int myScore = sc.nextInt();
		int P = sc.nextInt();
		
		int[] a = new int[51];

		for(int i = 0; i < N; i++){
			a[i] = sc.nextInt(); //점수
		}
		
		if(N == P && myScore <= a[N-1]){
			System.out.println(-1);
		}else{
			for(int i = 0; i < N; i++){
				if(myScore >= a[i]){
					System.out.println(i+1);
					return;
				}
			}
			System.out.println(N+1);	
		}//else
		
	}

}
