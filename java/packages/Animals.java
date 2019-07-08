package Animals;

 class mammalInt implements Animal{
	public void eat(){
		System.out.println("Animal eats");
	}
	
	public void travel(){
		System.out.println("Animal travels");
	}
	public int noOflegs(){
		return 0;
	}
}

class Animals{
	public static void main(String []args){
		mammalInt m=new mammalInt();
		m.eat();
		m.travel();
	}
}