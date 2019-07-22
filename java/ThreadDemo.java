class ThreadDemo extends Thread{
	public void run(){
		//
	}
	public static void main(String[] args){
		Thread t1=new Thread();
		System.out.println("Thread created");
		//t1.run();
		t1.start();
		//t1.sleep();
		//t1.terminate();
	}
}