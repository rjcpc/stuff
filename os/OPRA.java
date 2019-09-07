/*
Enter page frame sequence(separated by space):
Enter page replacement algo:
======= Optimal Page Replacement ===========
Initial Memory layout...
|‐1|‐1|‐1|
Loading page no.1:7
|7|‐1|‐1|
Loading page no.2:0
|7|0|‐1|
Loading page no.3:1
|7|0|1|
Loading page no.4:2
|2|0|1|
Loading page no.5:0
|2|0|1|
Loading page no.6:3
|2|0|3|
Loading page no.7:0
|2|0|3|
Loading page no.8:4
|2|4|3|
Loading page no.9:2
|2|4|3|
Loading page no.10:3
|2|4|3|
Loading page no.11:0
|2|0|3|
Loading page no.12:3
|2|0|3|
Loading page no.13:2
|2|0|3|
Loading page no.14:1
|2|0|1|
Loading page no.15:2
|2|0|1|
Loading page no.16:0
|2|0|1|
Loading page no.17:1
|2|0|1|
Loading page no.18:7
|7|0|1|
Loading page no.19:0
|7|0|1|
Loading page no.20:1
|7|0|1|
Total Number of page faults:9
*/

import java.io.*;  
class MemMgmt  
{  
String frame_sequence;  
int mem_block[];  
MemMgmt(String fs,int n)  
{  
frame_sequence = fs;  
mem_block = new int[n];  
for(int i=0;i<n; i++)  
mem_block[i]=-1;  
}  
void dispMemBlock()  
{  
System.out.print("|");  
for(int i=0;i<mem_block.length;i++)  
{  
System.out.print(mem_block[i]+"|");  
}  
System.out.println();  
}  
void fcfs()  
{  
System.out.println("======= FCFS ===========");  
String strpages[] = frame_sequence.split(" ");  
int pages[] = new int[strpages.length];  
for(int i=0; i<strpages.length; i++)  
pages[i] = Integer.parseInt(strpages[i]);  
int mem_block_num=0, page_faults=0;  
System.out.println("Initial Memory layout...");  
dispMemBlock();  
for(int i=0; i<pages.length; i++)  
{  
boolean present=false;  
for(int j=0;j<mem_block.length;j++)  
{  
if(mem_block[j] == pages[i])  
{  
present=true;  
break;  
}  
}  
if(!present)  
{  
mem_block[mem_block_num] = pages[i];  
mem_block_num++;  
page_faults++;  
}  
if(mem_block_num==mem_block.length)  
mem_block_num=0;  
System.out.println("Loading page no." + (i+1) + ":" + pages[i]);  
dispMemBlock();  
}  
System.out.println("Total Number of page faults:" + page_faults);  
}  
void oppr()  
{  
System.out.println("======= Optimal Page Replacement===========");  
String strpages[] = frame_sequence.split(" ");  
int pages[] = new int[strpages.length];  
int i=0;  
for(i=0; i<strpages.length; i++)  
pages[i] = Integer.parseInt(strpages[i]);  
int mem_block_num=0,page_faults=0;  
System.out.println("Initial Memory layout...");  
dispMemBlock();  
for(i=0; i<mem_block.length; i++)  
{  
boolean present=false;  
for(int j=0;j<mem_block.length;j++)  
{  
if(mem_block[j] == pages[i])  
{  
present=true;  
break;  
}  
}  
if(!present)  
{  
mem_block[mem_block_num] = pages[i];  
mem_block_num++;  
page_faults++;  
}  
System.out.println("Loading page no." + (i+1) + ":" + pages[i]);  
dispMemBlock();  
}  
for(; i<pages.length; i++)  
{  
boolean present=false;  
for(int j=0;j<mem_block.length;j++)  
{  
if(mem_block[j] == pages[i])  
{  
present=true;  
break;  
}  
}  
if(!present) 
 
{  
mem_block_num=-1;  
int longest_page=-1;  
for(int j=0;j<mem_block.length; j++)  
{  
int k=0;  
for(k=i+1; k<pages.length; k++)  
{  
if(mem_block[j] == pages[k])  
{  
if(k>longest_page)  
{  
longest_page = k;  
mem_block_num = j;  
}  
break;  
}  
}  
if(k==pages.length)  
{  
longest_page = pages.length;  
mem_block_num = j;  
}  
}  
mem_block[mem_block_num] = pages[i];  
page_faults++;  
}  
System.out.println("Loading page no." + (i+1) + ":" + pages[i]);  
dispMemBlock();  
}  
System.out.println("Total Number of page faults:" + page_faults);  
}  
}  
class OPRA  
{  
public static void main(String args[]) throws Exception  
{  
BufferedReader br = new BufferedReader(new  
InputStreamReader(System.in));  
System.out.println("Enter page frame sequence(separated by space):");  
//String frame_sequence = br.readLine();  
String frame_sequence = "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1";  
System.out.println("Enter page replacement algo:");  
int i = Integer.parseInt(br.readLine());  
MemMgmt m = new MemMgmt(frame_sequence,3);  
if(i==1)  
m.fcfs();  
else  
if(i==2)  
m.oppr();  
}  
} 
