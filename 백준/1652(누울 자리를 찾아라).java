/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/1652
*/

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		sc.nextLine();
		String[] s = new String[n];
		
		for(int i = 0; i < n; i++){
			s[i] = sc.nextLine();
		}
		
		int row = 0;
		int col = 0;
		
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				if(s[i].charAt(j) == '.'){
					//row
					if(j < n -1 && s[i].charAt(j+1) == '.'){
						if(j+2 == n)
							row++;
						else if(s[i].charAt(j+2) == 'X')
							row++;
					}
					
					//col
					if(i < n - 1 && s[i+1].charAt(j) == '.'){
						if(i+2 == n)
							col++;
						else if(s[i+2].charAt(j) == 'X')
							col++;
					}
				}
			}
		}//for
		
		System.out.println(row+ " " + col);
		
		
	}

}
