/*
Can be a voter
Exception occured : InvalidAgeException: invalid age
completed
*/
class InvalidAgeException extends Exception{
	InvalidAgeException(String s){
		super(s);
	}  
}   

class CustomException{
	static void validate(int age) throws InvalidAgeException{
		if (age<18){
			throw new InvalidAgeException("invalid age");
		}else{
			System.out.println("Can be a voter");
		}
	}
	
	public static void main(String[] args){
		try{
			validate(19);
			validate(15);
		}catch (Exception e){
			System.out.println("Exception occured : "+e);
		}finally{
			System.out.println("completed");
		}
	}
}
