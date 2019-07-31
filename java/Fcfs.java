import java.io.*;
class Fcfs
{
  public static void main(String args[])
throws Exception
{
    
    int n,AT[],BT[],WT[],TAT[];
    float AWT = 0;
    InputStreamReader isr=new InputStreamReader(System.in);
          BufferedReader br=new BufferedReader(isr);
System.out.println("Enter number of process");
    n=Integer.parseInt(br.readLine());

    BT=new int[n];
    WT=new int[n];
    TAT=new int[n];
    AT=new int[n];
System.out.println("enter burst time for each process\n");
    for(int i=0;i<n;i++)
{
System.out.println("Enter BT for process" + (i+1));
    BT[i]=Integer.parseInt(br.readLine());
}
    for(int i=0;i<n;i++)
{
System.out.println("enter at process"+i);
AT[i]=Integer.parseInt(br.readLine());
}
WT[0]=0;
for(int i=1;i<n;i++)
{
for(int i2=0;i2<i;i2++)
{
WT[i]=WT[i]-AT[i];
}
for(i=0;i<n;i++)
{
TAT[i]=WT[i]+BT[i];
AWT=AWT+WT[i];
}
System.out.println("PROCESS BT WT TAT");
for(i=0;i<n;i++)
{
System.out.println(" "+i+" "+BT[i]+" "+WT[i]+ " " +TAT[i]+ " ");
}
AWT=AWT/n;
System.out.println("Avg waiting time="+AWT);
}
}
}