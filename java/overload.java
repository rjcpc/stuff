class maths{
	public int multiply(int x,int y){
		return x*y;
	}
	public int multiply(int x,int y,int z){
		return x*y*z;
	}
	public double multiply(double x,double y){
		return x*y;
	}
	public double multiply(double x,double y,double z){
		return  x*y*z;
	}
}






class Overload{
	public static void main(String[] args){
		maths nums=new maths();
		System.out.println("\nThe multiplication of 2 ,3 is :\n"+	nums.multiply(2,3));
		System.out.println("\nThe multiplication of 2 ,3 ,4 is :\n"+nums.multiply(2,3,4));
		System.out.println("\nThe multiplication of 2.1 ,3.1 is :\n"+	nums.multiply(2.1,3.1));
		System.out.println("\nThe multiplication of 2.1 ,3.1 ,4.1 is :\n"+	nums.multiply(2.1,3.1,4.1));
	}
}