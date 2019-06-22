class RectangleNew{
	int length,breadth;
	void get_data(int length ,int breadth){
		this.length=length;
		this.breadth=breadth;
	
	
	}
	int area_rectangle(){
		int area=length*breadth;
		return area;
	}
	public static void main(String args[]){
		RectangleNew rect1=new RectangleNew();
		//rect1.length=10;
		//rect1.breadth=20;
		rect1.get_data(10,20);
		int answer=rect1.area_rectangle();
		System.out.println("Area is "+answer);
	}
	
	
}