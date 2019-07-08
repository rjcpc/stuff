package Calculator;


class AddSub extends Calculations{
	public int add(int x, int y){
		return x+y;
	}
	public int subtract(int x, int y){
		return x-y;
	}
}
class PackageDemo{
	public static void main(String []args){
		AddSub num1=new AddSub();
		//int ans1=num1.add(3,5);
		System.out.println("Addition of 3 and 5 is : "+ num1.add(3,5));
		AddSub num2=new AddSub();
		//int ans2=num2.subtract(3,5);
		System.out.println("Subtraction of 3 and 5 is : "+num2.subtract(3,5));
	}
}