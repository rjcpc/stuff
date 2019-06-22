class Rectangle{
	int length,breadth;
	void area_rectangle(){
		int area=length*breadth;
		System.out.println("area is "+area);
	}
	public static void main(String args[]){
		Rectangle rect1=new Rectangle();
		rect1.length=10;
		rect1.breadth=20;
		rect1.area_rectangle();
	}
	
	
}