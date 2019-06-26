class bank{
	
	int getRateOfInterest(){
		return 0;
	}
}
class sbi extends bank{
	
	int getRateOfInterest(){
		return 8;
	}
}
class boi extends bank{
	
	int getRateOfInterest(){
		return 7;
	}
}
class cbi extends bank{
	
	int getRateOfInterest(){
		return 9;
	}
}
class Override{
	public static void main(String[] args){
		bank bank1=new boi();
		bank bank2=new sbi();
		bank bank3=new cbi();
		System.out.println("Rate of interest for boi is : "+bank1.getRateOfInterest());
		System.out.println("Rate of interest for sbi is : "+bank2.getRateOfInterest());
		System.out.println("Rate of interest for cbi is : "+bank3.getRateOfInterest());
	}
}