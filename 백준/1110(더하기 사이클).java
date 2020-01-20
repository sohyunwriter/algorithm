import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int temp = 0;
		int cur = n;
		int len = 0;
		
		while(true){
			temp = cur%10 + cur/10;
			cur = (cur%10)*10 + temp%10;
			//System.out.println(temp + ", " + next);
			
			if(cur != n){
				len++;
			}else{
				len++;
				System.out.println(len);
				break;
			}
			
		}
	}

}
