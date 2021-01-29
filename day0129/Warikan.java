import java.util.*;
public class Warikan{
	public static void main(String[] args){
		System.out.print("料金を入力>>");
		Scanner sc=new Scanner(System.in);
		int price=sc.nextInt();
		System.out.print("人数を入力>>");
		int number=sc.nextInt();
		System.out.printf("お支払いは%d円です",price/number);
	}
}
