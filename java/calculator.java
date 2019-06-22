class Add{
	int x=5; int y=4;
	void add_method(){
		System.out.println("addition is "+(x+y));
	}
	
}

class Sub{
	int x=5; int y=4;
	void sub_method(){
		System.out.println("subtraction is "+(x-y));
	}
	
}





class Calculator{
	public static void main(String args[]){
		Add num1=new Add();
		num1.add_method();
		Sub num2=new Sub();
		num2.sub_method();
	}
	
	
}