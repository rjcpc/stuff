interface math{
	int add(int x,int y);
}
class addition implements math{
	public int add(int x,int y){
		return x+y;
	}
}

class InterfaceDemo{
	public static void main(String[] args){
		addition nums=new addition();
		System.out.println("The Addition of 4 and 5 is :"+nums.add(4,5));
	}
	
	
}