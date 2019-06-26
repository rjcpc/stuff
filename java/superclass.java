class Add{
	int addnum(int x,int y){
		return (x+y);
	}
}

class Mul extends Add {
	
	int mulnum(int x,int y){
		int ans=0;
		for (int i=0;i<y;i++){
			ans=super.addnum(x,ans);
		}
		
		return (ans);
	}
}
class SuperClass{
	public static void main(String[] args){
		Mul nums=new Mul();
		
		System.out.println("The Multiplication of 3 and 15 is :"+nums.mulnum(15,3));
	}
}