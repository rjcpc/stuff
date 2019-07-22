class Table{
	synchronized void printTable(int n){
		for(int i=1;i<=5;i++){
			System.out.println(n*i);
		}
		try{
			System.out.println("Wait 3 seconds...");
			Thread.sleep(3000);
		}catch(Exception e){
			System.out.println("catch");
		}
	}
}

class NewThread1 extends Thread{
	Table t;
	NewThread1(Table t){
		this.t=t;
	}
	public void run(){
		t.printTable(5);
	}
}
class NewThread2 extends Thread{
	Table t;
	NewThread2(Table t){
		this.t=t;
	}
	public void run(){
		t.printTable(100);
	}
}
public class SynchDemo{
	public static void main(String[] args){
		Table obj=new Table();
		NewThread1 t1=new NewThread1(obj);
		NewThread2 t2=new NewThread2(obj);
		t1.start();
		t2.start();
	}
}