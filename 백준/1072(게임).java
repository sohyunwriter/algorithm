/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1072
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long X = sc.nextInt();
		long Y = sc.nextInt();
		
		long ans = 0;
		long Z = (Y * 100) / X;
	
		if(Z >= 99) {
			ans = -1;
		}
		else {
			long temp1 = X * (Z + 1) - 100*Y;
			long temp2 = 99 - Z;
			if (temp1 % temp2 == 0)
				ans = temp1 / temp2;
			else
				ans = temp1 / temp2 + 1;
		}
		
		System.out.println(ans);
		
	}

}
