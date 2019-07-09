class Consumer implements Runnable{
	Stock c;
	Thread t;
	Consumer(Stock c){
		this.c=c;
		t=new Thread(this,"Producer thread");
		t.start();
	}
	public void run(){
		while(true){
			try{
				t.sleep(750);
				
			}catch(Exception e){
				c.getstock((int)(Math.random()*1000));
				
			}
			
		}
	}
	void stop(){
		t.stop();
	}
}

class Producer implements Runnable{
	Stock s;
	Thread t;
	Producer(Stock s){
		this.s=s;
		t=new Thread(this,"Producer thread");
		t.start();
	}
	public void run(){
		while(true){
			try{
				t.sleep(750);
				
			}catch(Exception e){
				//
				
			}
			s.addstock((int)(Math.random()*1000));
		}
	}
	void stop(){
		t.stop();
		
	}
}

public class Stock{
	int goods=0;
	
	public synchronized void addstock(int i){
		goods=goods+i;
		System.out.println("stock added: "+i);
		System.out.println("present stock: "+goods);
		notify();
	}
	public synchronized int getstock(int j){
		while(true){
			if(goods>=j){
				goods=goods-j;
				System.out.println("Stock taken away :"+j);
				System.out.println("Present stock: "+goods);
				break;
			}else{
				System.out.println("Stock not enough");
				System.out.println("Waiting for stocks to come");
				try{
					wait();
				}catch(Exception e){
					//
				}
			}
		}
		return goods;
	}
	
	public static void main(String []args){
		Stock j=new Stock();
		Producer p=new Producer(j);
		Consumer c=new Consumer(j);
		try{
			Thread.sleep(10000);
			p.stop();
			c.stop();
			System.out.println("Thread stopped");
			
		}catch(Exception e){
			//
		}
		System.exit(0);
	}
}