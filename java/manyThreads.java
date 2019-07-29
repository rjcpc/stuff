class Customer{
	int amount=10000;
	synchronized void withdraw(int amount){
		System.out.println("Going to withdraw");
		if(this.amount<amount){
			System.out.println("Less balance, waiting for deposit");
			try{
				wait();	
			}catch(Exception e){
				//
			}
		}
		this.amount -= amount;
		System.out.println("Withdraw complete");
	}
	synchronized void deposit(int amount){
		System.out.println("Going to deposit");
		this.amount += amount;
		System.out.println("Deposit complete");
		notify();
	}
}
class ManyThreads {
	public static void main(String []args){
		final Customer c=new Customer();
		Thread t1=new Thread(){
			public void run(){
				c.withdraw(15000);
				
			};
		};
		t1.start();
		Thread t2=new Thread(){
			public void run(){
				c.deposit(15000);
				
			};
		};
		t2.start();
	}
	
}