
package practical1;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class Practical1 extends JFrame implements ActionListener,ItemListener{
    JLabel l1,l2,l3;
    JTextField t1,t2;
    JComboBox jcb;
    JButton b1,b2;
    String s="";
    Practical1(){
    l1=new JLabel("Enter Number ");
    l2=new JLabel("Choose");
    l3=new JLabel("Result");
    t1=new JTextField(20);
    t2=new JTextField(20);
    jcb=new JComboBox();
    b1=new JButton("Calculate");
    b2=new JButton("clear");
    
    jcb.addItem("Square");
    jcb.addItem("Cube");
    Container cp=getContentPane();
    cp.setLayout(new FlowLayout());
    
    cp.add(l1);
    cp.add(t1);
    cp.add(l2);
    cp.add(jcb);
    cp.add(l3);
    cp.add(t2);
    cp.add(b1);
    cp.add(b2);
    
    jcb.addItemListener(this);
    b1.addActionListener(this);
    b2.addActionListener(this);
    
    setSize(700,700);
    setVisible(true);
    }
    
    public void itemStateChanged(ItemEvent ie){  
     s=(String)ie.getItem();
    }
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource()==b1){
            int x=Integer.parseInt(t1.getText());
            int y;
            if(s.equals("Square")){
                y=x*x;
            }else{
                
                y=x*x*x;
            }
            t2.setText(y+"");
        }else{
        t1.setText("");
        t2.setText("");
        t1.requestFocus();
        } 
    }
    public static void main(String[] args) {      
       new Practical1();           
    }  
}
