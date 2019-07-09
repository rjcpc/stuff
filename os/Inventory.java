class InventoryFunc{
	static int qoh=500;
	static int req=0;
	static public void request(int order){
		if (order<=qoh){
			System.out.println("Quantity ordered:"+qoh);
			qoh-=order;
			req+=order;
			System.out.println("Quantity at hand:"+qoh);
			System.out.println("Total quantity taken away by way of order:"+req);
		}else{
			System.out.println("Ordered quantity more than quantity at hand");
		}
	}
}

class Inventory{
	public static void main(String []args){
		new TestThread();
		try{
			for (int i=3;i>0;i--){
				System.out.println("----------");
				System.out.println("Main thread : "+i);
				System.out.println("----------");
				Thread.sleep(1000);
			}
		}catch(InterruptedException e){
			System.out.println("Exiting main thread..");
		}
	}
}

class TestThread extends Thread{
	TestThread(){
		super("Test Thread");
		System.out.println("Child thread:"+this);
		start();
		
	}
	public void run(){
		for(int i=5;i>0;i--){
			try{
				sleep(100);
				
			}catch(InterruptedException e){
				System.out.println("I="+i);
				
			}
			InventoryFunc.request((int)(Math.random()*100));
		}
	}
}