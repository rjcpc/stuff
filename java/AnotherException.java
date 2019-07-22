class NegativeException extends Exception{
	NegativeException(String s){
		super(s);
	}
	
}
class AnotherException{
	
	public static void check(int num) throws NegativeException{
		if (num<0){
			throw new NegativeException("Entered a negative Number");
		}else{
			System.out.println("Positive number");
		}
	}
	public static void main(String[] args){
		try{
			check(44);
			check(-44);
		}catch(Exception e){
			System.out.println("Exception : "+e);
		}finally{
			System.out.println("Completed");
		}
		
	}
}