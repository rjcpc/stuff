class mathops{
	String  stufff="Multiple classes";
	
}

class AddSub extends mathops {
	
	void addnum(int x,int y){
		System.out.println("the addition of "+x+" and "+y+" is : "+(x+y));
	}
	void subnum(int x, int y){
		System.out.println("the subtraction of "+x+" and "+y+" is : "+(x-y));
	}
}
class Mul extends AddSub{
	void mulnum(int x ,int y){
		System.out.println("the multiplication of "+x+" and "+y+" is : "+(x*y));
	}
	
	
}


class Division extends Mul{
	void divnum(int x ,int y){
		System.out.println("the Division of "+x+" and "+y+" is : "+(x/y));
	}
	
	
}


class InheritClass{
	public static void main(String args[]){
		Division demo=new Division();
		demo.addnum(6,7);
		demo.subnum(7,30);
		demo.mulnum(5,7);
		demo.divnum(35,7);
		System.out.println(demo.stufff);
	}
	
	
}