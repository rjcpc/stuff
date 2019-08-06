//WARNING---
//this program has errors ??
import java.io.*;
class job implements Runnable{
	int process_id ,no_of_instructions,time_quantum;
	Thread t;
	job(int pid, int instr,int tq){
		process_id=pid;
		no_of_instructions=instr;
		time_quantum=tq;
		t=new Thread(this);
		t.start();
		
	}
	public void run(){
		try{
			for(int i=1;i<=no_of_instructions;i++){
				System.out.println("Job "+process_id+" is over");
				
			}
		}catch(Exception e){
			System.out.println("The job has been interrupted..");
		}
	}
}
class rr{
	public static void main(String[] args){
		try{
			int process_id,time_quantum;
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Enter a user process starting number: ");
			process_id=Integer.parseInt(br.readLine());
			System.out.println("Enter atime quantum in millisecond: ");
			time_quantum=Integer.parseInt(br.readLine());
			job j1=new job(++process_id,10,time_quantum);
			job j2=new job(++process_id,6,time_quantum);
			job j3=new job(++process_id,8,time_quantum);
		}catch(Exception e){
			System.out.println("Some process failed to complete..");
			System.out.println("plz contact system admin...");
		}
	}
}