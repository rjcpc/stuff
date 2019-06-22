class Computer{
	void computer_method(){
		System.out.println("computer_method");
	}
}

class Laptop{
	void laptop_method(){
		System.out.println("laptop_method");
	}
	
	
	public static void main(String args[]){
		Computer comp=new Computer();
		comp.computer_method();
		
		
		Laptop lap=new Laptop();
		lap.laptop_method();
	}

	
}


