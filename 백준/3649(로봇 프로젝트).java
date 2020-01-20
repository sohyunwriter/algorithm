/*
Name : Sohyeon Yim
Email : brightcattle@gmail.com 
Blog : https://sohyunwriter.tistory.com/
Problem : https://www.acmicpc.net/problem/3649
*/

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNext()){
			int width = sc.nextInt();
			int n = sc.nextInt();
			int[] a = new int[n];
			width *= 10000000;
			
			for(int i = 0; i < n; i++){
				a[i] = sc.nextInt();
			}
			
			Arrays.sort(a);
			
			int l = 0; 
			int r = n-1;
			
			while(l < r){
				if(a[l] + a[r] == width && l != r){
					System.out.println("yes "+ a[l] + " " + a[r]);
					break;
				}
				else if(a[l] + a[r] > width){
					r-= 1;
				}
				else if(a[l] + a[r] < width){
					l+= 1;
				}
				
			}//while
			
			if(l >= r)
				System.out.println("danger");
			
		}
	}

}
