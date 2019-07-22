class ExceptionDemo{
	public static void main(String[] args){
		
		try{
			int a=6;
			int b=0;
			int c=a/b;
			System.out.println("The value is: "+c);
		}catch(Exception e){
			System.out.println("Incorrect code: "+e);
		}finally{
			System.out.println("Completed");
		}
	}
}