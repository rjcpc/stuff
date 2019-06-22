class AddFunc{
	int num1,num2;
	int ans;
	
	AddFunc(){
		System.out.println("default constructor");
	}
	AddFunc(int num1,int  num2){
		this.num1=num1;
		this.num2=num2;
		System.out.println("constructor with parameter");
	}
	int sum(){
		int total=num1+num2;
		return total;

	}
	public static void main (String args[]){
		AddFunc first=new AddFunc();
		first.num1=10;
		first.num2=20;
		first.ans=first.sum();
		AddFunc second=new AddFunc(20,40);
		second.ans=second.sum();
		System.out.println("The sum is : "+ first.ans +" and "+ second.ans);
	}

}